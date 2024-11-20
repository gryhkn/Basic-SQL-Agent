# __import__('pysqlite3')
# import sys
# sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from sqlalchemy import create_engine, inspect, text
import pandas as pd
from llama_index import SQLDatabase
from llama_index.llms import OpenAI
from llama_index.indices.struct_store import NLSQLTableQueryEngine
import openai
import os
from dotenv import load_dotenv

load_dotenv() 
# OpenAI setup
openai.api_key = os.environ["OPENAI_API_KEY"]


llm = OpenAI(temperature=0, model="gpt-4", streaming=True)

def create_streamlit_ui():
    st.set_page_config(
        page_title="User Database Chat",
        layout="centered",
        initial_sidebar_state="auto",
    )

    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "Hello! Ask me anything about the users in the database."}
        ]

    st.title("User Database Chat 💬")
    st.info(
        "I can help you query information about users, like their age, email, or when they were created.", 
        icon="ℹ️"
    )

def create_sidebar():
    sql_database, engine = load_db()

    st.sidebar.markdown("## Database Schema")
    inspector = inspect(engine)
    table_names = inspector.get_table_names()
    selected_table = st.sidebar.selectbox("Select a table", table_names)

    with engine.connect() as con:
        query = "SELECT * FROM users LIMIT 30"
        df = pd.read_sql_query(query, con)

    st.sidebar.text(f"Sample data from '{selected_table}':")
    st.sidebar.dataframe(df)

def load_db():
    engine = create_engine("sqlite:///test_users.db")
    sql_database = SQLDatabase(engine, include_tables=["users"])
    return sql_database, engine

def main():
    sql_database, engine = load_db()

    sql_query_engine = NLSQLTableQueryEngine(
        sql_database=sql_database,
        tables=["users"],
    )

    if "query_engine" not in st.session_state:
        st.session_state["query_engine"] = sql_query_engine

    # Display chat history
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask about the users:"):
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state["messages"].append({"role": "user", "content": prompt})

        # Generate response
        if st.session_state["messages"][-1]["role"] != "assistant":
            with st.spinner():
                with st.chat_message("assistant"):
                    response = sql_query_engine.query(prompt)
                    response_text = str(response)
                    st.write(response_text)
                    st.session_state["messages"].append(
                        {"role": "assistant", "content": response_text}
                    )

if __name__ == "__main__":
    create_streamlit_ui()
    create_sidebar()
    main()
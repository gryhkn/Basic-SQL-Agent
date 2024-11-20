# Simple SQL ChatBot

## Overview

A basic chatbot that queries a SQLite database using natural language. Built with LlamaIndex and Streamlit.

## Features

- Natural language queries to SQL database
- Simple user interface
- Sample database with 50 test users
- Real-time chat interface

## Quick Start

1. Clone the repo
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Add your OpenAI API key in `app.py`
4. Run the database setup:

```
python setup_db.py
```

5. Start the app:

```
streamlit run app.py
```

## Tech Stack

- Streamlit
- LlamaIndex
- SQLite
- OpenAI GPT-4o

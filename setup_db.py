import sqlite3
from datetime import datetime

# Create a database connection
conn = sqlite3.connect("test_users.db")  # Creates an SQLite file named test_users.db.
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

# Create sample data
users = [
    ("john_doe1", "john1@example.com", 25),
    ("jane_doe2", "jane2@example.com", 30),
    ("mark_smith3", "mark3@example.com", 28),
    ("lisa_brown4", "lisa4@example.com", 22),
    ("paul_jones5", "paul5@example.com", 35),
    ("emily_davis6", "emily6@example.com", 27),
    ("daniel_white7", "daniel7@example.com", 31),
    ("laura_clark8", "laura8@example.com", 24),
    ("mike_moore9", "mike9@example.com", 26),
    ("sarah_hall10", "sarah10@example.com", 29),
    ("alex_taylor11", "alex11@example.com", 32),
    ("chris_wilson12", "chris12@example.com", 33),
    ("nina_harris13", "nina13@example.com", 21),
    ("george_martin14", "george14@example.com", 36),
    ("anna_king15", "anna15@example.com", 23),
    ("david_lewis16", "david16@example.com", 28),
    ("olivia_walker17", "olivia17@example.com", 27),
    ("josh_baker18", "josh18@example.com", 29),
    ("lily_green19", "lily19@example.com", 25),
    ("ryan_adams20", "ryan20@example.com", 30),
    ("amelia_hill21", "amelia21@example.com", 34),
    ("jacob_scott22", "jacob22@example.com", 31),
    ("chloe_mitchell23", "chloe23@example.com", 22),
    ("noah_morgan24", "noah24@example.com", 20),
    ("mia_rogers25", "mia25@example.com", 29),
    ("ethan_cooper26", "ethan26@example.com", 33),
    ("sophia_reed27", "sophia27@example.com", 26),
    ("mason_bell28", "mason28@example.com", 28),
    ("isabella_wright29", "isabella29@example.com", 27),
    ("logan_hughes30", "logan30@example.com", 35),
    ("ava_foster31", "ava31@example.com", 23),
    ("elijah_butler32", "elijah32@example.com", 24),
    ("emma_simmons33", "emma33@example.com", 30),
    ("lucas_fisher34", "lucas34@example.com", 26),
    ("harper_cook35", "harper35@example.com", 32),
    ("jack_russell36", "jack36@example.com", 27),
    ("ella_patterson37", "ella37@example.com", 25),
    ("oliver_griffin38", "oliver38@example.com", 21),
    ("sophia_peters39", "sophia39@example.com", 29),
    ("james_long40", "james40@example.com", 34),
    ("charlotte_hayes41", "charlotte41@example.com", 20),
    ("liam_watson42", "liam42@example.com", 33),
    ("ava_price43", "ava43@example.com", 24),
    ("benjamin_brooks44", "benjamin44@example.com", 28),
    ("scarlett_ward45", "scarlett45@example.com", 22),
    ("henry_bennett46", "henry46@example.com", 30),
    ("grace_evans47", "grace47@example.com", 23),
    ("theo_stevens48", "theo48@example.com", 31),
    ("zara_edwards49", "zara49@example.com", 26),
    ("oscar_perry50", "oscar50@example.com", 27)
]

# Insert data
cursor.executemany("INSERT INTO users (username, email, age) VALUES (?, ?, ?)", users)

# Save changes to the database
conn.commit()

# Read the database to check after insertion
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()

import os
import sqlite3
from pathlib import Path

APP_NAME = "Please Remind Me"
DATABASE_FILENAME = "reminders.db"
DATABASE_PATH = Path(os.environ.get("LOCALAPPDATA", Path.home())) / APP_NAME / DATABASE_FILENAME

def get_connection():
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def initialize_database():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS recurring (
                id INTEGER PRIMARY KEY,
                title TEXT,
                enabled INTEGER,
                interval TEXT,
                created TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS one_time (
                id INTEGER PRIMARY KEY,
                title TEXT,
                enabled INTEGER,
                scheduled_time TEXT
            )
            """
        )

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS daily (
                id INTEGER PRIMARY KEY,
                title TEXT,
                enabled INTEGER,
                time TEXT,
                days TEXT
            )
            """
        )

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS pomodoro (
                id INTEGER PRIMARY KEY,
                title TEXT,
                enabled INTEGER,
                created TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS twenty (
                id INTEGER PRIMARY KEY,
                title TEXT,
                enabled INTEGER,
                created TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


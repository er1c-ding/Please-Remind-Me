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

def load_reminders_from_database(app):
    with get_connection() as connection:
        recurring_reminders = connection.execute("SELECT title, interval FROM recurring").fetchall()
        one_time_reminders = connection.execute("SELECT title, scheduled_time FROM one_time").fetchall()
        daily_reminders = connection.execute("SELECT title, time, days FROM daily").fetchall()
        pomodoro_reminders = connection.execute("SELECT title FROM pomodoro").fetchall()
        twenty_reminders = connection.execute("SELECT title FROM twenty").fetchall()

    for reminder in recurring_reminders:
        app.reminder_container.create_frame(
            type = "Recurring",
            title = reminder["title"],
            widget_values = [reminder["interval"]]
        )

    for reminder in one_time_reminders:
        date, time = reminder["scheduled_time"].split(" ", 1)

        app.reminder_container.create_frame(
            type = "One Time",
            title = reminder["title"],
            widget_values = [date, time]
        )

    for reminder in daily_reminders:
        app.reminder_container.create_frame(
            type = "Daily",
            title = reminder["title"],
            widget_values = reminder["days"].split(",") +  [reminder["time"]]
        )

    for reminder in pomodoro_reminders:
        app.reminder_container.create_frame(
            type = "Pomodoro",
            title = reminder["title"],
            widget_values = []
        )

    for reminder in twenty_reminders:
        app.reminder_container.create_frame(
            type = "20-20-20",
            title = reminder["title"],
            widget_values = []
        )

def initialize_database():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS recurring (
                id INTEGER PRIMARY KEY,
                title TEXT,
                enabled INTEGER,
                interval TEXT
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
                enabled INTEGER
            )
            """
        )

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS twenty (
                id INTEGER PRIMARY KEY,
                title TEXT,
                enabled INTEGER
            )
            """
        )

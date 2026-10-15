import os
import sqlite3
from pathlib import Path
import config

APP_NAME = "Please Remind Me"
DATABASE_FILENAME = "reminders.db"
DATABASE_PATH = Path(os.environ.get("LOCALAPPDATA", Path.home())) / APP_NAME / DATABASE_FILENAME

REMINDER_TABLE_DICT = {
    "Recurring": "recurring",
    "One Time": "one_time",
    "Daily": "daily",
    "Pomodoro": "pomodoro",
    "20-20-20": "twenty",
}

def get_connection():
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def delete_reminder(reminder_type, reminder_id):
    table = REMINDER_TABLE_DICT[reminder_type]
    with get_connection() as connection:
        connection.execute(f"DELETE FROM {table} WHERE id = ?", (reminder_id,))

def load_reminders_from_database(app):
    with get_connection() as connection:
        recurring_reminders = connection.execute("SELECT id, title, interval, enabled FROM recurring").fetchall()
        one_time_reminders = connection.execute("SELECT id, title, scheduled_time, enabled FROM one_time").fetchall()
        daily_reminders = connection.execute("SELECT id, title, time, days, enabled FROM daily").fetchall()
        pomodoro_reminders = connection.execute("SELECT id, title, enabled FROM pomodoro").fetchall()
        twenty_reminders = connection.execute("SELECT id, title, enabled FROM twenty").fetchall()
        max_reminder_id = connection.execute(
            """
            SELECT MAX(id) AS max_id FROM (
                SELECT id FROM recurring
                UNION ALL SELECT id FROM one_time
                UNION ALL SELECT id FROM daily
                UNION ALL SELECT id FROM pomodoro
                UNION ALL SELECT id FROM twenty
            )
            """
        ).fetchone()["max_id"]

    for reminder in recurring_reminders:
        config.reminder_count = reminder["id"]
        app.reminder_container.create_frame(
            type = "Recurring",
            title = reminder["title"],
            widget_values = [reminder["interval"]],
            force_enabled = bool(reminder["enabled"])
        )

    for reminder in one_time_reminders:
        config.reminder_count = reminder["id"]
        date, time = reminder["scheduled_time"].split(" ", 1)

        app.reminder_container.create_frame(
            type = "One Time",
            title = reminder["title"],
            widget_values = [date, time],
            force_enabled = bool(reminder["enabled"])
        )

    for reminder in daily_reminders:
        config.reminder_count = reminder["id"]
        app.reminder_container.create_frame(
            type = "Daily",
            title = reminder["title"],
            widget_values = reminder["days"].split(",") +  [reminder["time"]],
            force_enabled = bool(reminder["enabled"])
        )

    for reminder in pomodoro_reminders:
        config.reminder_count = reminder["id"]
        app.reminder_container.create_frame(
            type = "Pomodoro",
            title = reminder["title"],
            widget_values = [],
            force_enabled = bool(reminder["enabled"])
        )

    for reminder in twenty_reminders:
        config.reminder_count = reminder["id"]
        app.reminder_container.create_frame(
            type = "20-20-20",
            title = reminder["title"],
            widget_values = [],
            force_enabled = bool(reminder["enabled"])
        )

    config.reminder_count = 0 if max_reminder_id is None else max_reminder_id

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

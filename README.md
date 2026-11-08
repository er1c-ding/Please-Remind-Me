# Please Remind Me

**Please Remind Me** is a Python desktop app for everyday tasks, recurring reminders, and work breaks. Create reminders through a CustomTkinter interface and receive desktop notifications when they are due.

Reminders are saved locally with SQLite and restored when you reopen the app, including whether each reminder is enabled or disabled.

## Features

| Reminder type | Schedule |
| --- | --- |
| Recurring | Repeat at a custom interval in hours, minutes, and seconds. |
| Daily | Send a reminder at a specific time on selected days of the week. |
| One Time | Send a reminder at a specific date and time, then automatically remove it. |
| Pomodoro | Alternate between 25-minute work periods and 5-minute breaks. |
| 20-20-20 | Prompt you to look away after 20 minutes, then look back after 20 seconds. |

- Create reminders in a separate window and manage them in a scrollable list.
- Enable or disable individual reminders without deleting them.
- Delete reminders you no longer need.
- Automatically save reminder settings and enabled states between sessions.
- Receive desktop notifications through Plyer.

## Installation on Windows

**Download the project → build the `.exe` → run the `.exe`.**

These steps package the Python source into a Windows application using PyInstaller. Build it on Windows. Python is needed to build the application; it is not needed to run the finished bundle.

### 1. Download the project

1. Open the [Please Remind Me repository](https://github.com/er1c-ding/Please-Remind-Me).
2. Select **Code → Download ZIP**.
3. Right-click the downloaded ZIP and select **Extract All**.
4. Open the extracted project folder containing `main.py`.

### 2. Install Python and the required packages

Install a current supported Python 3 release from [python.org](https://www.python.org/downloads/windows/), including Tkinter support and the Python launcher. If the installer offers **Add Python to PATH**, enable it. Reopen your terminal after installation.

In File Explorer, open the folder containing `main.py`, right-click an empty area, and select **Open in Terminal**. Use PowerShell for the commands below.

Create an isolated Python environment and install the app's dependencies and build tool:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install customtkinter plyer pyinstaller
```

If `py` is unavailable but `python --version` works, use `python -m venv .venv` for the first command. The remaining commands stay the same.

Tkinter and SQLite are included with the standard Python installation; they do not need separate pip packages. There is currently no `requirements.txt` in this repository.

Before packaging, check that the app opens from source:

```powershell
.\.venv\Scripts\python.exe main.py
```

Close the app before continuing.

### 3. Convert the project into a Windows `.exe`

Run this command from the same project folder:

```powershell
.\.venv\Scripts\python.exe -m PyInstaller --noconfirm --onedir --windowed --name "Please Remind Me" --collect-all customtkinter --hidden-import plyer.platforms.win.notification main.py
```

This bundles the app, Python runtime, CustomTkinter assets, and Plyer's Windows notification backend. The `--windowed` option opens the app without a separate console window.

The result is an application folder:

```text
dist/
└── Please Remind Me/
    ├── Please Remind Me.exe
    └── _internal/
```

This uses PyInstaller's folder-based build so the executable and its supporting files stay together. See the [PyInstaller options](https://pyinstaller.org/en/stable/usage.html) and [CustomTkinter packaging guidance](https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging) for details.

### 4. Run the `.exe`

1. Open `dist`, then open the `Please Remind Me` folder.
2. Double-click **Please Remind Me.exe**.
3. Select **CREATE NEW REMINDER** to add your first reminder.

You can move or share the entire `Please Remind Me` folder. Keep `_internal` beside the `.exe`; copying only the executable will leave out required files. To make the app easier to launch, create a desktop shortcut to the executable.

Keep the app running and your computer awake to receive reminders. Closing the window exits the app; it does not continue running in the system tray or start automatically with Windows.

## Using the app

1. Select **CREATE NEW REMINDER**.
2. Choose a reminder type from the dropdown.
3. For Recurring, Daily, or One Time reminders, enter a title and schedule. Pomodoro and 20-20-20 use built-in schedules.
4. Select **SAVE**. New reminders start enabled.
5. Use a reminder's switch to enable or disable it, or select **DELETE** to remove it permanently.

Enter times as `HH:MM:SS` using a 24-hour clock and dates as `DD/MM/YYYY`. For recurring reminders, enter a positive interval. For daily reminders, select at least one day of the week. Input validation is still being improved, so check your entries before saving.

Schedules use your computer's local date and time. Enabled recurring, Pomodoro, and 20-20-20 reminders restart their timing cycles when the app is reopened or the reminder is re-enabled; countdown progress is not saved.

## Saved reminders

On Windows, the app automatically creates its database at:

```text
%LOCALAPPDATA%\Please Remind Me\reminders.db
```

Paste `%LOCALAPPDATA%\Please Remind Me` into File Explorer's address bar to open that folder. The database stores reminder settings and enabled states separately from the source code and executable. You do not need to bundle or manually create a database file.

To back up your reminders, close the app and copy this database to a safe location. Sharing the application folder does not include your saved reminders.

## Troubleshooting

- **Python is not found:** Reopen the terminal after installing Python. Try `python` instead of `py` when creating the environment.
- **The executable does not open:** Make sure the whole application folder, including `_internal`, is present. Run the source command from step 2 in a terminal to check for errors.
- **The source runs but the executable fails:** Rebuild with the command in step 3, replacing `--windowed` with `--console`, then launch the executable from PowerShell to read the error output.
- **Notifications do not appear:** Check Windows notification settings and Do Not Disturb, and confirm that the reminder is enabled and the app is still running.

## Project structure

```text
Please-Remind-Me/
├── main.py          # Startup, database initialization, and main event loop
├── gui.py           # Main window, reminder creation, and reminder controls
├── frames.py        # Input forms for each reminder type
├── reminders.py     # Reminder classes, schedules, and notifications
├── timer.py         # Checks enabled reminders every second
├── database.py      # SQLite storage, loading, and deletion
├── config.py        # Shared styles, widgets, and application state
├── README.md
└── LICENSE
```

The app uses a shared `Reminder` base class with subclasses for each schedule. Tkinter's event loop checks reminders periodically, while SQLite stores their settings between sessions.

## Project status

This is a personal project built to practice object-oriented programming, desktop GUI development, event-driven scheduling, and local data persistence.

Potential improvements include editing existing reminders, stronger input validation, more reliable scheduling after sleep or downtime, automated tests, and further interface improvements.

## License

This project is licensed under the [MIT License](LICENSE).

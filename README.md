# Please Remind Me

**Please Remind Me** is a desktop reminder application built with Python and CustomTkinter. It allows users to create and manage several types of reminders through a graphical interface.

## Features

- Recurring reminders with customizable intervals
- Daily reminders for specific days and times
- One-time reminders for specific dates and times
- Pomodoro work/break reminders
- 20-20-20 eye-rest reminders
- Enable/disable controls for individual reminders
- Desktop notifications
- Dynamic reminder creation
- Scrollable reminder list

## Technical Highlights

### Object-Oriented Design

The application uses a common `Reminder` base class with specialized subclasses for different reminder behaviors.

This allows shared functionality such as enabling and disabling reminders to remain in the base class while each reminder type handles its own scheduling logic.

### Event-Driven Scheduling

The application uses Tkinter's event loop to periodically check active reminders.

When a reminder reaches its scheduled time, the application triggers a desktop notification and calculates the next scheduled event.

### Modular Architecture

The project separates the GUI, reminder logic, and scheduling system into different modules:

- `main.py` — application entry point
- `gui.py` — main application windows and reminder management
- `frames.py` — reminder creation interfaces
- `reminders.py` — reminder classes and scheduling logic
- `timer.py` — scheduling loop
- `config.py` — shared application state and configuration

## Technologies

- Python
- CustomTkinter
- Tkinter
- Plyer
- Object-oriented programming
- Event-driven programming

## Project Structure

```text
Please-Remind-Me/
├── main.py
├── gui.py
├── frames.py
├── reminders.py
├── timer.py
├── config.py
├── requirements.txt
└── LICENSE
```

## Motivation

I built this project as a practical way to learn and apply object-oriented programming, GUI development, event-driven programming, and application state management.

The project also gave me experience designing multiple related features around a shared architecture instead of implementing each feature as a separate program.

## Next Steps

- Add persistent storage using SQL
- Add editing for existing reminders
- Improve input validation and error handling
- Improve scheduling reliability
- Add additional reminder types
- Improve UI/UX
- Add automated tests

## Project Status

**Personal project — actively being improved.**

The current version implements the core reminder functionality and application architecture. Future development will focus on persistence, reliability, testing, and expanding the feature set.

## License

MIT License
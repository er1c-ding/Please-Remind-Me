Please Remind Me

Please Remind Me is a desktop reminder application built with Python and CustomTkinter. It lets users create and manage different types of reminders through a simple GUI, including recurring reminders, scheduled reminders, Pomodoro timers, and the 20-20-20 eye-rest rule.

What I Built

I designed the application around a single reminder system that supports multiple reminder behaviors rather than creating separate programs for each use case.

The application currently supports:

Recurring reminders — repeat at a user-defined interval
Daily reminders — schedule reminders for specific days and times
One-time reminders — schedule a reminder for a specific date and time
Pomodoro reminders — alternate between work and break periods
20-20-20 reminders — alternate between 20 minutes of work and 20 seconds of looking away
Enable/disable controls for individual reminders
Dynamic reminder creation through the GUI
Desktop notifications when reminders trigger
Scrollable reminder list for managing multiple reminders
Technical Highlights
Object-Oriented Design

Different reminder behaviors are represented using separate classes derived from a common Reminder base class.

This allows shared functionality such as enabling/disabling reminders to remain in the base class while each reminder type implements its own scheduling behavior.

Event-Driven Scheduling

The application uses Tkinter's event loop to periodically check whether an active reminder is ready to trigger.

When a reminder's scheduled time is reached, the application sends a desktop notification and calculates the next scheduled event.

Modular GUI

The interface is separated into multiple modules:

gui.py — main application windows and reminder management
frames.py — reminder creation interfaces
reminders.py — reminder logic and scheduling
timer.py — scheduling loop and notifications
config.py — shared UI configuration and application state
main.py — application entry point

This separation keeps the GUI, scheduling logic, and reminder models from being tightly coupled.

Technologies
Python
CustomTkinter
Tkinter
Plyer — desktop notifications
Object-oriented programming
Event-driven programming
Project Structure
Please-Remind-Me/
├── main.py
├── gui.py
├── frames.py
├── reminders.py
├── timer.py
├── config.py
├── requirements.txt
└── LICENSE
Why I Built It

I wanted to build a practical desktop application while learning more about object-oriented programming, GUI development, event-driven programming, and managing state across different components of an application.

The project also gave me an opportunity to think about how several related features could share a common architecture instead of being implemented independently.

Future Improvements

Some areas I would like to explore as the project develops:

Persistent storage using a database
Editing existing reminders
Improved input validation and error handling
More flexible scheduling
Additional reminder types
Improved UI/UX
Automated tests
Project Status

Personal project — actively being improved.

The current version focuses on the core reminder functionality and application architecture. Future development will focus on persistence, reliability, and expanding the feature set.

License

MIT License
Please Remind Me

Please Remind Me is a desktop reminder application built with Python and CustomTkinter. It allows users to create different types of reminders and manage them through a graphical user interface.

Features
Create and manage multiple reminders
Recurring reminders at a specified time
Daily reminders on selected days of the week
One-time reminders for a specific date and time
Pomodoro timer
20-20-20 eye-strain reminder
Enable or disable individual reminders
Delete reminders through the GUI
Scrollable reminder list
Desktop GUI built with CustomTkinter
Screenshots

Screenshots coming soon.

Installation
Requirements
Python 3
CustomTkinter
Any other dependencies listed in requirements.txt
Setup
Clone the repository:
git clone https://github.com/er1c-ding/Please-Remind-Me.git
cd Please-Remind-Me
Create a virtual environment:
python -m venv .venv
Activate the virtual environment.

Windows:

.venv\Scripts\activate

macOS/Linux:

source .venv/bin/activate
Install the dependencies:
pip install -r requirements.txt
Run the application:
python main.py
Usage

After launching the application, use Create New Reminder to select the type of reminder you want to create.

Depending on the reminder type, you can configure its title, schedule, or other available options. Created reminders appear in the main window and can be enabled, disabled, or deleted.

Project Structure
Please-Remind-Me/
├── main.py          # Application entry point
├── gui.py           # Main GUI and reminder interface
├── reminders.py     # Reminder and timer logic
├── frames.py        # GUI frames used for reminder creation
├── config.py        # Application configuration and shared state
└── requirements.txt # Python dependencies
Technologies
Python
CustomTkinter
Tkinter
Project Status

This is a personal project that is still under development. Future improvements may include persistent reminder storage, additional reminder types, and other quality-of-life features.

License

This project is licensed under the MIT License.
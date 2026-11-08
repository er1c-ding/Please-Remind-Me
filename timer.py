import config
import datetime
import reminders
import database

class Timer():
    """Check reminders through the GUI event loop."""

    def __init__(self, app):
        """Store the app used to schedule reminder checks."""
        self.app = app
    
    def start_timer(self):
        """Schedule the first reminder check."""
        self.app.after(1, self.check)

    def check(self):
        """Run due reminders, remove completed ones, and schedule another check."""
        curr_time = datetime.datetime.now().replace(microsecond = 0)

        for reminder in config.reminders:
            if reminder.enabled:
                reminder.execute(curr_time)

        # Remove completed one-time reminders from storage and the interface.
        for reminder in config.reminders:
            if type(reminder) == reminders.One_Time_Reminder and reminder.perma_disabled:
                for frame in config.reminder_frames:
                    if frame.reminder == reminder:
                        frame.self_destruct()
                        break

        # Schedule the next check without blocking the GUI event loop.
        self.app.after(1000, self.check)
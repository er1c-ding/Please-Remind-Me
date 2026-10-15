import config
import datetime
import reminders
import database

class Timer():
    def __init__(self, app):
        self.app = app
    
    def start_timer(self):
        self.app.after(1, self.check)

    def check(self):
        curr_time = datetime.datetime.now().replace(microsecond = 0)

        for reminder in config.reminders:
            if reminder.enabled:
                reminder.execute(curr_time)

        for reminder in config.reminders:
            if type(reminder) == reminders.One_Time_Reminder and reminder.perma_disabled:
                for frame in config.reminder_frames:
                    if frame.reminder == reminder:
                        frame.self_destruct()
                        break

        self.app.after(1000, self.check)
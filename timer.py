import config
import datetime
import reminders
from plyer import notification

class Timer():
    def __init__(self, app):
        self.app = app
    
    def start_timer(self):
        self.app.after(1, self.check)

    def check(self):
        curr_time = datetime.datetime.now().replace(microsecond = 0)

        for reminder in config.reminders:
            if reminder.enabled:
                if type(reminder) == reminders.Recurring_Reminder:
                    if reminder.next_time <= curr_time:
                        self.send_notification(reminder.title, "It's time for your reminder: " + reminder.title)
                        reminder.next()
                elif type(reminder) == reminders.Daily_Reminder:
                    if reminder.next_time <= curr_time:
                        self.send_notification(reminder.title, "It's time for your reminder: " + reminder.title)
                        reminder.next()
                elif type(reminder) == reminders.One_Time_Reminder:
                    if reminder.time <= curr_time:
                        self.send_notification(reminder.title, "It's time for your reminder: " + reminder.title)
                        reminder.next()
                elif type(reminder) == reminders.Twenty_Reminder:
                    if reminder.next_time <= curr_time:
                        if reminder.cycle % 2 == 1:
                            self.send_notification(reminder.title, "It's time to look away!")
                        else:
                            self.send_notification(reminder.title, "It's time to look back!")
                        reminder.next()
                elif type(reminder) == reminders.Pomodoro_Reminder:
                    if reminder.next_time <= curr_time:
                        if reminder.cycle % 2 == 1:
                            self.send_notification(reminder.title, "It's time for work!")
                        else:
                            self.send_notification(reminder.title, "It's time for your break!")
                        reminder.next()

        for reminder in config.reminders:
            if type(reminder) == reminders.One_Time_Reminder and reminder.perna_disabled:
                config.reminders.remove(reminder)

        self.app.after(1000, self.check)

    def send_notification(self, title, description):
        notification.notify(title = title, message = description, app_name = "Please Remind Me", timeout = 3)
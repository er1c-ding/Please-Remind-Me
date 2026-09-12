from datetime import datetime, timedelta
import config
from plyer import notification

class Reminder():
    reminder_count = 0

    def __init__(self, title, enabled):
        self.reminder_id = Reminder.reminder_count
        Reminder.reminder_count += 1
        self.title = title
        self.enabled = enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def execute(self):
        pass

    def send_notification(self, title, description):
        notification.notify(title = title, message = description, app_name = "Please Remind Me", timeout = 3)

class Recurring_Reminder(Reminder):
    def __init__(self, title, enabled, interval):
        super().__init__(title, enabled)
        self.start_time = None
        self.interval_datetime = timedelta(seconds = int(interval.split(':')[2]), minutes = int(interval.split(':')[1]), hours = int(interval.split(':')[0]))
        self.next_time = None

    def next(self):
        self.start_time = self.next_time
        self.next_time = self.start_time + self.interval_datetime

    def enable(self):
        self.enabled = True
        self.start_time = datetime.now().replace(microsecond = 0)
        self.next_time = self.start_time + self.interval_datetime

    def execute(self, curr_time):
        if self.next_time <= curr_time:
            super().send_notification(self.title, "It's time for your reminder: " + self.title)
            self.next()

class One_Time_Reminder(Reminder):
    def __init__(self, title, enabled, date, time):
        super().__init__(title, enabled)
        self.next_time = datetime.strptime(date + " " + time, "%d/%m/%Y %H:%M:%S")
        self.perma_disabled = False

    def next(self):
        for frame in config.reminder_frames:
            if frame.reminder == self:
                frame.destroy()
                config.reminder_frames.remove(frame)
                self.perma_disabled = True
                self.enabled = False
                break

    def enable(self):
        if not self.perma_disabled:
            self.enabled = True

    def execute(self, curr_time):
        if self.next_time <= curr_time:
            super().send_notification(self.title, "It's time for your reminder: " + self.title)
            self.next()

class Daily_Reminder(Reminder):
    def __init__(self, title, enabled, days, time):
        super().__init__(title, enabled)
        self.days_arr = []

        days_of_week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

        for day in days:
            if day == "EVERYDAY":
                self.days_arr.extend([0, 1, 2, 3, 4, 5, 6])
            elif day == "WEEKDAYS":
                self.days_arr.extend([0, 1, 2, 3, 4])
            elif day == "WEEKENDS":
                self.days_arr.extend([5, 6])
            else:
                self.days_arr.append(days_of_week.index(day))

        self.time = datetime.strptime(time, "%H:%M:%S")
        self.next_time = None

    def next(self):
        self.next_time = self.next_time + timedelta(days = 1)

        while self.next_time.weekday() not in self.days_arr:
            self.next_time += timedelta(days = 1)

    def enable(self):
        self.enabled = True
        self.next_time = datetime.now().replace(microsecond = 0)
        self.next_time = self.next_time.replace(hour = self.time.hour, minute = self.time.minute, second = self.time.second)

        while self.next_time.weekday() not in self.days_arr:
            self.next_time += timedelta(days = 1)

    def execute(self, curr_time):
        if self.time <= curr_time:
            super().send_notification(reminder.title, "It's time for your reminder: " + reminder.title)
            self.next()

class Pomodoro_Reminder(Reminder):
    def __init__(self, title, enabled):
        super().__init__(title, enabled)
        self.start_time = None
        self.next_time = None
        self.cycle = 1

    def next(self):
        if self.cycle % 2 == 0:
            self.start_time = self.next_time
            self.next_time = self.start_time + timedelta(minutes = 25)
        else:
            self.start_time = self.next_time
            self.next_time = self.start_time + timedelta(minutes = 5)
        self.cycle += 1

    def enable(self):
        self.enabled = True
        self.start_time = datetime.now().replace(microsecond = 0)
        self.next_time = self.start_time + timedelta(minutes = 25)
        self.cycle = 1

    def execute(self, curr_time):
        if self.next_time <= curr_time:
            if self.cycle % 2 == 1:
                super().send_notification(self.title, "It's time to look away!")
            else:
                super().send_notification(self.title, "It's time to look back!")
            self.next()

class Twenty_Reminder(Reminder):
    def __init__(self, title, enabled):
        super().__init__(title, enabled)
        self.start_time = None
        self.next_time = None
        self.cycle = 1

    def next(self):
        if self.cycle % 2 == 0:
            self.start_time = self.next_time
            self.next_time = self.start_time + timedelta(minutes = 20)
        else:
            self.start_time = self.next_time
            self.next_time = self.start_time + timedelta(seconds = 20)
        self.cycle += 1

    def enable(self):
        self.enabled = True
        self.start_time = datetime.now().replace(microsecond = 0)
        self.next_time = self.start_time + timedelta(minutes = 20)
        self.cycle = 1

    def execute(self, curr_time):
        if self.next_time <= curr_time:
            if self.cycle % 2 == 1:
                super().send_notification(self.title, "It's time for work!")
            else:
                super().send_notification(self.title, "It's time for your break!")
                self.next()
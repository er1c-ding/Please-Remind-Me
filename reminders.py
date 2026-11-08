from datetime import datetime, timedelta
from plyer import notification
import database
import config

class Reminder():
    """Provide shared reminder state and notification support."""

    reminder_count = 0

    def __init__(self, title, enabled):
        """Store the reminder ID, title, and enabled state."""
        self.reminder_id = config.reminder_count
        self.title = title
        self.enabled = enabled

    def enable(self):
        """Enable the reminder."""
        self.enabled = True

    def disable(self):
        """Disable the reminder."""
        self.enabled = False

    def execute(self):
        """Provide a no-op execution hook for reminder subclasses."""
        pass

    def send_notification(self, title, description):
        """Send a desktop notification with the given title and message."""
        notification.notify(title = title, message = description, app_name = "Please Remind Me", timeout = 3)

class Recurring_Reminder(Reminder):
    """Repeat notifications at a fixed interval."""

    def __init__(self, title, enabled, interval):
        """Parse the interval and start scheduling if enabled."""
        super().__init__(title, enabled)
        self.start_time = None
        self.interval_datetime = timedelta(seconds = int(interval.split(':')[2]), minutes = int(interval.split(':')[1]), hours = int(interval.split(':')[0]))
        self.next_time = None

        if self.enabled:
            self.enable()

    def next(self):
        """Advance the next notification by one interval."""
        self.start_time = self.next_time
        self.next_time = self.start_time + self.interval_datetime

    def enable(self):
        """Restart the interval and save the enabled state."""
        self.enabled = True
        self.start_time = datetime.now().replace(microsecond = 0)
        self.next_time = self.start_time + self.interval_datetime

        with database.get_connection() as connection:
            connection.execute(
                "UPDATE recurring SET enabled = ? WHERE id = ?",
                (self.enabled, self.reminder_id)
            )

    def disable(self):
        """Disable the reminder and save its state."""
        self.enabled = False

        with database.get_connection() as connection:
            connection.execute(
                "UPDATE recurring SET enabled = ? WHERE id = ?",
                (self.enabled, self.reminder_id)
            )

    def execute(self, curr_time):
        """Send a notification if due and advance the schedule."""
        if self.next_time <= curr_time:
            super().send_notification(self.title, "It's time for your reminder: " + self.title)
            self.next()

class One_Time_Reminder(Reminder):
    """Send a single notification at a specified date and time."""

    def __init__(self, title, enabled, date, time):
        """Parse the scheduled date and time and set the initial state."""
        super().__init__(title, enabled)
        self.next_time = datetime.strptime(date + " " + time, "%d/%m/%Y %H:%M:%S")
        self.perma_disabled = False

        if self.enabled:
            self.enable()

    def next(self):
        """Mark the reminder complete and disable it."""
        self.perma_disabled = True
        self.disable()

    def enable(self):
        """Enable an unfinished reminder and save its state."""
        if not self.perma_disabled:
            self.enabled = True

        with database.get_connection() as connection:
            connection.execute(
                "UPDATE one_time SET enabled = ? WHERE id = ?",
                (self.enabled, self.reminder_id)
            )

    def disable(self):
        """Disable the reminder and save its state."""
        self.enabled = False

        with database.get_connection() as connection:
            connection.execute(
                "UPDATE one_time SET enabled = ? WHERE id = ?",
                (self.enabled, self.reminder_id)
            )

    def execute(self, curr_time):
        """Send a notification if due and mark the reminder complete."""
        if self.next_time <= curr_time:
            super().send_notification(self.title, "It's time for your reminder: " + self.title)
            self.next()

class Daily_Reminder(Reminder):
    """Repeat notifications at a set time on selected weekdays."""

    def __init__(self, title, enabled, days, time):
        """Parse the selected days and time and schedule if enabled."""
        super().__init__(title, enabled)
        self.days_arr = []

        days_of_week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

        # Expand saved day labels into weekday numbers (Monday = 0).
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

        if self.enabled:
            self.enable()

    def next(self):
        """Advance to the next selected day."""
        self.next_time = self.next_time + timedelta(days = 1)

        while self.next_time.weekday() not in self.days_arr:
            self.next_time += timedelta(days = 1)

    def enable(self):
        """Schedule the time on a selected day and save the enabled state."""
        self.enabled = True
        self.next_time = datetime.now().replace(microsecond = 0)
        self.next_time = self.next_time.replace(hour = self.time.hour, minute = self.time.minute, second = self.time.second)

        while self.next_time.weekday() not in self.days_arr:
            self.next_time += timedelta(days = 1)

        with database.get_connection() as connection:
            connection.execute(
                "UPDATE daily SET enabled = ? WHERE id = ?",
                (self.enabled, self.reminder_id)
            )

    def disable(self):
        """Disable the reminder and save its state."""
        self.enabled = False

        with database.get_connection() as connection:
            connection.execute(
                "UPDATE daily SET enabled = ? WHERE id = ?",
                (self.enabled, self.reminder_id)
            )

    def execute(self, curr_time):
        """Send a notification if due and advance to the next selected day."""
        if self.next_time <= curr_time:
            super().send_notification(self.title, "It's time for your reminder: " + self.title)
            self.next()

class Pomodoro_Reminder(Reminder):
    """Alternate 25-minute work periods and 5-minute breaks."""

    def __init__(self, title, enabled):
        """Initialize the work and break cycle and start if enabled."""
        super().__init__(title, enabled)
        self.start_time = None
        self.next_time = None
        self.cycle = 1

        if self.enabled:
            self.enable()

    def next(self):
        """Schedule the next work or break period."""
        if self.cycle % 2 == 0:
            self.start_time = self.next_time
            self.next_time = self.start_time + timedelta(minutes = 25)
        else:
            self.start_time = self.next_time
            self.next_time = self.start_time + timedelta(minutes = 5)
        self.cycle += 1

    def enable(self):
        """Restart the 25-minute work period and save the enabled state."""
        self.enabled = True
        self.start_time = datetime.now().replace(microsecond = 0)
        self.next_time = self.start_time + timedelta(minutes = 25)
        self.cycle = 1

        with database.get_connection() as connection:
            connection.execute(
                "UPDATE pomodoro SET enabled = ? WHERE id = ?",
                (self.enabled, self.reminder_id)
            )

    def disable(self):
        """Disable the reminder and save its state."""
        self.enabled = False

        with database.get_connection() as connection:
            connection.execute(
                "UPDATE pomodoro SET enabled = ? WHERE id = ?",
                (self.enabled, self.reminder_id)
            )

    def execute(self, curr_time):
        """Send the due cycle notification and advance to the next period."""
        if self.next_time <= curr_time:
            if self.cycle % 2 == 1:
                super().send_notification(self.title, "It's time for work!")
            else:
                super().send_notification(self.title, "It's time for your break!")
            self.next()

class Twenty_Reminder(Reminder):
    """Alternate 20-minute screen periods and 20-second eye breaks."""

    def __init__(self, title, enabled):
        """Initialize the eye-rest cycle and start if enabled."""
        super().__init__(title, enabled)
        self.start_time = None
        self.next_time = None
        self.cycle = 1

        if self.enabled:
            self.enable()

    def next(self):
        """Schedule the next screen period or eye break."""
        if self.cycle % 2 == 0:
            self.start_time = self.next_time
            self.next_time = self.start_time + timedelta(minutes = 20)
        else:
            self.start_time = self.next_time
            self.next_time = self.start_time + timedelta(seconds = 20)
        self.cycle += 1

    def enable(self):
        """Restart the 20-minute screen period and save the enabled state."""
        self.enabled = True
        self.start_time = datetime.now().replace(microsecond = 0)
        self.next_time = self.start_time + timedelta(minutes = 20)
        self.cycle = 1

        with database.get_connection() as connection:
            connection.execute(
                "UPDATE twenty SET enabled = ? WHERE id = ?",
                (self.enabled, self.reminder_id)
            )

    def disable(self):
        """Disable the reminder and save its state."""
        self.enabled = False

        with database.get_connection() as connection:
            connection.execute(
                "UPDATE twenty SET enabled = ? WHERE id = ?",
                (self.enabled, self.reminder_id)
            )

    def execute(self, curr_time):
        """Send the due eye-rest notification and advance the cycle."""
        if self.next_time <= curr_time:
            if self.cycle % 2 == 1:
                super().send_notification(self.title, "It's time to look away!")
            else:
                super().send_notification(self.title, "It's time to look back!")
            self.next()

from datetime import datetime

class Reminder():
    reminder_count = 0

    def __init__(self, enabled):
        self.reminder_id = Reminder.reminder_count
        Reminder.reminder_count += 1
        self.enabled = enabled

class Recurring_Reminder(Reminder):
    def __init__(self, enabled, interval):
        super().__init__(enabled)
        self.interval = interval
        self.start_time = datetime.now().replace(microsecond=0)
        self.next_time = None

class One_Time_Reminder(Reminder):
    def __init__(self, enabled, date, time):
        super().__init__(enabled)
        self.time = None

class Daily_Reminder(Reminder):
    def __init__(self, enabled, days, time):
        super().__init__(enabled)
        self.time = None

class Podomuro_Reminder(Reminder):
    def __init__(self, enabled, cycle):
        super().__init__(enabled)
        self.start_time = datetime.now().replace(microsecond=0)
        self.next_time = None

class Twenty_Reminder(Reminder):
    def __init__(self, enabled, cycle):
        super().__init__(enabled)
        self.start_time = datetime.now().replace(microsecond=0)
        self.next_time = None
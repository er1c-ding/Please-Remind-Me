from datetime import datetime

class Reminder():
    reminder_count = 0

    def __init__(self, enabled):
        self.reminder_id = Reminder.reminder_count
        Reminder.reminder_count += 1

        self.start_time = datetime.now().replace(microsecond=0)
        self.enabled = enabled
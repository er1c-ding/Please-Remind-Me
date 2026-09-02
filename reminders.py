class Reminder():
    reminder_count = 0

    def __init__(self, start_time, next_time, enabled):
        self.reminder_id = Reminder.reminder_count
        Reminder.reminder_count += 1

        self.start_time = start_time
        self.next_time = next_time
        self.enabled = enabled
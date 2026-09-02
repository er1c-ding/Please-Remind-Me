import customtkinter as ctk
import config
import frames

class New_Reminder_Window(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Create New Reminder")

        coord_x = self.winfo_screenwidth() // 2 - 190
        coord_y = self.winfo_screenheight() // 2 - 300
        self.geometry(f"580x600+{coord_x}+{coord_y}")

        self.protocol("WM_DELETE_WINDOW", self.destroy)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.configure(fg_color = config.BACKGROUND)

        self.curr_option_val = ctk.StringVar(value = "Select Option")

        self.option_menu = ctk.CTkOptionMenu(
            master = self,
            values = ["Select Option", "Recurring", "Daily", "One Time", "Podomuro", "20-20-20"],
            variable = self.curr_option_val,
            fg_color = config.BUTTON,
            button_color = config.BUTTON,
            text_color = config.TEXT,
            font = config.BODY_FONT,
            dropdown_font = config.SMALL_FONT,
            dropdown_fg_color = config.BUTTON,
            dropdown_text_color = config.TEXT,
            command = self.switch_frame
        )

        self.option_menu.pack(anchor = "w", padx = (20, 0), pady = (20, 0))

        self.creation_frame = frames.Creation_Frame(
            master = self
        )

        self.creation_frame.pack(anchor = "w", pady = (20, 0))

    def switch_frame(self, value):
        self.creation_frame.destroy()

        if value == "Select Option":
            self.creation_frame = frames.Creation_Frame(master = self)
        elif value == "Recurring":
            self.creation_frame = frames.Recurring_Frame(master = self)
        elif value == "Daily":
            self.creation_frame = frames.Daily_Frame(master = self)
        elif value == "One Time":
            self.creation_frame = frames.One_Time_Frame(master = self)
        elif value == "Podomuro":
            self.creation_frame = frames.Default_Frame(master = self, type = "Podomuro")
        else:
            self.creation_frame = frames.Default_Frame(master = self, type = "20-20-20")

        self.creation_frame.pack(anchor = "w", pady = (20, 0))

    def save(self):
        type_value = self.curr_option_val.get()
        title_value = None
        widget_values_value = []

        if type_value in ["Recurring", "Daily", "One Time"]:
            title_value = self.creation_frame.title_var.get()
        else:
            title_value = type_value

        if type_value == "One Time":
            month_value = self.creation_frame.month.get().zfill(2)
            day_value = self.creation_frame.day.get().zfill(2)
            year_value = self.creation_frame.year.get().zfill(2)

            widget_values_value.append(f"{month_value}/{day_value}/{year_value}")

        if type_value == "Daily":
            days_of_week_values = []
            days_of_week_names = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

            for i in range(7):
                value = self.creation_frame.checkbox_frame.days_of_week[i].get()
                days_of_week_values.append(value)

            if days_of_week_values[:5] == ['1', '1', '1', '1', '1']:
                widget_values_value.append("WEEKDAYS")
            else:
                print(days_of_week_values)
                for i in range(5):
                    if days_of_week_values[i] == '1':
                        widget_values_value.append(days_of_week_names[i])

            if days_of_week_values[5:] == ['1', '1']:
                widget_values_value.append("WEEKENDS")
            else:
                for i in range(5, 7):
                    if days_of_week_values[i] == '1':
                        widget_values_value.append(days_of_week_names[i])

        if type_value in ["Recurring", "Daily", "One Time"]:
            seconds_value = self.creation_frame.seconds.get().zfill(2)
            minutes_value = self.creation_frame.minutes.get().zfill(2)
            hours_value = self.creation_frame.hours.get().zfill(2)

            widget_values_value.append(f"{hours_value}:{minutes_value}:{seconds_value}")

        self.master.reminder_container.create_frame(type_value, title_value, widget_values_value)

        self.destroy()

class Reminder_Frame(ctk.CTkFrame):
    reminder_count = 0

    def __init__(self, master, type, title, widget_values, **kwargs):
        super().__init__(master, **kwargs)

        self.reminder_id = Reminder_Frame.reminder_count
        Reminder_Frame.reminder_count += 1

        self.configure(
            width = 480,
            height = 120,
            corner_radius = 5,
            fg_color = "#C5E2FF"
        )

        self.grid_propagate(False)

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1, minsize=80)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.reminder_title = ctk.CTkLabel(
            self,
            text = title,
            text_color = config.TEXT,
            font = config.SUBTITLE_FONT
        )

        self.reminder_title.grid(column = 0, row = 0, columnspan = 6, sticky = "w", padx = 20, pady = (10, 0))

        self.reminder_type = config.Default_Label(
            self,
            text = type
        )

        self.reminder_type.grid(column = 0, row = 0, columnspan = 6, sticky = "e", padx = 20, pady = (10, 0))

        if len(widget_values) < 4:
            for i in range(len(widget_values)):
                self.specific_date = config.Default_DateTime_Widget(
                    self,
                    text = widget_values[i],
                )

                if i == 0:
                    self.specific_date.grid(column = i, row = 1, sticky = "w", padx = (20, 0))
                else:
                    self.specific_date.grid(column = i, row = 1, sticky = "w", padx = 0)
        else:
            self.specific_date = config.Default_DateTime_Widget(self, text = widget_values[0])
            self.specific_date.grid(column = 0, row = 1, sticky = "w", padx = (20, 0))

            self.specific_date = config.Default_DateTime_Widget(self, text = widget_values[len(widget_values) - 1])
            self.specific_date.grid(column = 1, row = 1, sticky = "w")

            self.specific_date = config.Default_DateTime_Widget(self, text = "+" + str(len(widget_values) - 2) + " MORE")
            self.specific_date.grid(column = 2, row = 1, sticky = "w")

        self.delete = config.Default_Little_Button(
            self,
            width = 25,
            height = 22,
            text = "DELETE",
            command = lambda: self.self_destruct()
        )

        self.delete.grid(column = 0, row = 2, columnspan = 6, sticky = "w", padx = (20, 0), pady = 10)

        self.curr_toggle = ctk.StringVar(value = "off")
        
        self.toggle = ctk.CTkSwitch(
            self,
            text = "Disabled",
            variable = self.curr_toggle,
            onvalue = "on",
            offvalue = "off",
            text_color = config.TEXT,
            font = config.BODY_FONT,
            fg_color = "#BE6868",
            progress_color = "#8EEB71",
            command = self.enable_disable
        )

        self.toggle.grid(column = 0, row = 2, sticky = "e", columnspan = 6, pady = 10, padx = 20)

    def self_destruct(self):
        config.reminders.remove(self)
        self.destroy()

    def enable_disable(self):
        if self.curr_toggle.get() == "off":
            self.toggle.configure(text = "Disabled")
        else:
            self.toggle.configure(text = "Enabled")

class Reminder_Container(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(
            width = 500,
            height = 450,
            corner_radius = 10,
            fg_color = config.FRAME_BACKGROUND,
            scrollbar_button_color = "#738FBA"
        )

    def create_frame(self, type, title, widget_values):
        self.reminder = Reminder_Frame(
            master = self,
            type = type,
            title = title,
            widget_values = widget_values
        )
        
        self.reminder.pack(pady = (10,0))

        config.reminders.append(self.reminder)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Please Remind Me")

        coord_x = self.winfo_screenwidth() // 2 - 200
        coord_y = self.winfo_screenheight() // 2 - 400
        self.geometry(f"600x800+{coord_x}+{coord_y}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.configure(fg_color = config.BACKGROUND)

        self.title_text = ctk.CTkLabel(
            self,
            text = "Please Remind Me",
            justify = "center",
            text_color = config.TEXT,
            font = config.TITLE_FONT
        )

        self.title_text.pack(pady = (50,20))

        self.description = config.Default_Label(
            self,
            text = "The one stop convenient reminder app to prevent you \n from forgetting things",
            justify = "center"
        )
        self.description.pack()

        self.reminder_container = Reminder_Container(
            master = self
        )

        self.create_new = config.Default_Button(
            self,
            width = 300,
            height = 50,
            text = "CREATE NEW REMINDER",
            command = self.create_new_reminder
        )

        self.create_new.pack(pady = (30,0))
        
        self.reminder_container.pack(pady = (30,0))

        self.new_reminder_window = None

    def create_new_reminder(self):
        self.new_reminder_window = New_Reminder_Window(self)
        self.new_reminder_window.wm_transient(self) 
        self.new_reminder_window.lift()
        self.new_reminder_window.focus()
import customtkinter as ctk

BACKGROUND = "#BDDDFC"
FRAME_BACKGROUND = "#AED6FE"
TEXT = "#6A89A7"
BUTTON = "#88BDF2"
LITTLE_BUTTON = "#ABD3FA"
reminders = []

class New_Reminder_Window(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Create New Reminder")

        coord_x = self.winfo_screenwidth() // 2 - 190
        coord_y = self.winfo_screenheight() // 2 - 300
        self.geometry(f"580x600+{coord_x}+{coord_y}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.configure(fg_color = BACKGROUND)

        self.curr_option_val = ctk.StringVar(value = "Select Option")

        self.option_menu = ctk.CTkOptionMenu(
            master = self,
            values = ["Select Option", "Recurring", "Day-to-Day", "One Time", "Podomuro", "20-20-20"],
            variable = self.curr_option_val,
            fg_color = BUTTON,
            button_color = BUTTON,
            text_color = TEXT,
            font = ("Consolas", 18),
            dropdown_font = ("Consolas", 16),
            dropdown_fg_color = BUTTON,
            dropdown_text_color = TEXT
        )

        self.option_menu.pack(anchor = "w", padx = (20, 0), pady = (20, 0))

class Reminder_Frame(ctk.CTkFrame):
    def __init__(self, master, info, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(
            width = 480,
            height = 120,
            corner_radius = 5,
            fg_color = "#C5E2FF"
        )

        self.grid_propagate(False)

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.reminder_title = ctk.CTkLabel(
            self,
            text = "Reminder Name",
            text_color = TEXT,
            font = ("Consolas", 22)
        )

        self.reminder_title.grid(column = 0, row = 0, columnspan = 5, sticky = "w", padx = 20, pady = (10, 0))

        self.reminder_type = ctk.CTkLabel(
            self,
            text = "Reminder Type",
            text_color = TEXT,
            font = ("Consolas", 18)
        )

        self.reminder_type.grid(column = 5, row = 0, columnspan = 3, sticky = "e", padx = 20, pady = (10, 0))

        for i in range(3):
            self.specific_date = ctk.CTkLabel(
                self,
                text = "12/34/5678",
                text_color = TEXT,
                font = ("Consolas", 11),
                corner_radius = 10,
                height = 20,
                fg_color = BACKGROUND,
                padx = 2
            )

            if i == 0:
                PADDY = (20, 0)
            else:
                PADDY = 0

            self.specific_date.grid(column = i, row = 1, sticky = "w", padx = PADDY)

        self.delete = ctk.CTkButton(
            self,
            width = 25,
            height = 22,
            text = "X",
            anchor = "center",
            fg_color = LITTLE_BUTTON,
            text_color = TEXT,
            font = ("Consolas", 16),
            command = lambda: self.self_destruct()
        )

        self.delete.grid(column = 0, row = 2, sticky = "w", padx = (20, 0), pady = 10)

        self.edit = ctk.CTkButton(
            self,
            width = 75,
            height = 22,
            text = "EDIT",
            anchor = "center",
            fg_color = LITTLE_BUTTON,
            text_color = TEXT,
            font = ("Consolas", 16)
        )

        self.edit.grid(column = 0, row = 2, columnspan = 2, pady = 10)

        self.curr_toggle = ctk.StringVar(value = "off")
        
        self.toggle = ctk.CTkSwitch(
            self,
            text = "Enable",
            variable = self.curr_toggle,
            onvalue = "on",
            offvalue = "off",
            text_color = TEXT,
            font = ("Consolas", 16),
            fg_color = "#BE6868",
            progress_color = "#8EEB71",
            command = self.enable_disable
        )

        self.toggle.grid(column = 6, row = 2, columnspan = 2, pady = 10)

    def self_destruct(self):
        reminders.remove(self)
        self.destroy()

    def enable_disable(self):
        if self.curr_toggle.get() == "off":
            self.toggle.configure(text = "Enable")
        else:
            self.toggle.configure(text = "Disable")

class Reminder_Container(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(
            width = 500,
            height = 450,
            corner_radius = 10,
            fg_color = FRAME_BACKGROUND,
            scrollbar_button_color = "#738FBA"
        )

    def create_new_reminder(self):
        self.reminder = Reminder_Frame(
            master = self,
            info = None
        )
        
        self.reminder.pack(pady = (10,0))

        reminders.append(self.reminder)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Please Remind Me")

        coord_x = self.winfo_screenwidth() // 2 - 200
        coord_y = self.winfo_screenheight() // 2 - 400
        self.geometry(f"600x800+{coord_x}+{coord_y}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.configure(fg_color = BACKGROUND)

        self.title_text = ctk.CTkLabel(
            self,
            text = "Please Remind Me",
            justify = "center",
            text_color = TEXT,
            font = ("Consolas", 45)
        )

        self.title_text.pack(pady = (50,20))

        self.description = ctk.CTkLabel(
            self,
            text = "The one stop convenient reminder app to prevent you \n from forgetting things",
            justify = "center",
            text_color = TEXT,
            font = ("Consolas", 18)
        )
        self.description.pack()

        self.reminder_container = Reminder_Container(
            master = self
        )

        self.create_new = ctk.CTkButton(
            self,
            width = 300,
            height = 50,
            text = "CREATE NEW REMINDER",
            anchor = "center",
            fg_color = BUTTON,
            text_color = TEXT,
            font = ("Consolas", 20),
            command = self.reminder_container.create_new_reminder
        )

        self.create_new.pack(pady = (30,0))
        
        self.reminder_container.pack(pady = (30,0))

        self.new_reminder_window = New_Reminder_Window(self)

        self.new_reminder_window.wm_transient(self) 

        self.new_reminder_window.after(100, self.new_reminder_window.lift)
        self.new_reminder_window.after(100, self.new_reminder_window.focus)
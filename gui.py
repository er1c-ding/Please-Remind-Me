import customtkinter as ctk

BACKGROUND = "#BDDDFC"
FRAME_BACKGROUND = "#AED6FE"
TEXT = "#6A89A7"
BUTTON = "#88BDF2"

class Reminder_Container(ctk.CTkScrollableFrame):
     def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x800")
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

        self.create_new = ctk.CTkButton(
            self,
            width = 300,
            height = 50,
            text = "CREATE NEW REMINDER",
            anchor = "center",
            fg_color = BUTTON,
            text_color = TEXT,
            font = ("Consolas", 20)
        )

        self.create_new.pack(pady = (30,0))

        self.reminder_container = Reminder_Container(
            master = self,
            width = 500,
            height = 450,
            corner_radius = 10,
            fg_color = FRAME_BACKGROUND,
            scrollbar_button_color = "#738FBA"
        )

        self.reminder_container.pack(pady = (30,0))
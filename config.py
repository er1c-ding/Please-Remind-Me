import customtkinter as ctk

BACKGROUND = "#BDDDFC"
FRAME_BACKGROUND = "#AED6FE"
TEXT = "#3C5271"
BUTTON = "#88BDF2"
LITTLE_BUTTON = "#ABD3FA"
PLACEHOLDER_TEXT = "#4E5963"
ENTRY_BACKGROUND = "#DAEFFF"
TITLE_FONT = ("Consolas", 45)
SUBTITLE_FONT = ("Consolas", 22)
BUTTON_FONT = ("Consolas", 20)
BODY_FONT = ("Consolas", 18)
SMALL_FONT = ("Consolas", 16)
MICRO_FONT = ("Consolas", 11)
reminders = []

class Default_Entry(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(
            font = BODY_FONT,
            fg_color = ENTRY_BACKGROUND,
            text_color = TEXT,
            placeholder_text_color = PLACEHOLDER_TEXT,
            border_width = 0,
            justify = "center"
        )

class Default_Label(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(
            text_color = TEXT,
            font = BODY_FONT
        )

class Default_Button(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(
            fg_color = BUTTON,
            text_color = TEXT,
            font = BUTTON_FONT,
            anchor = "center"
        )

class Default_Little_Button(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(
            fg_color = LITTLE_BUTTON,
            text_color = TEXT,
            font = BODY_FONT,
            anchor = "center"
        )

class Default_Save_Button(Default_Button):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(
            height = 40,
            width = 100,
            text = "SAVE"
        )

class Default_Title_Entry(Default_Entry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(
            width = 450,
            placeholder_text = "Enter Title Here"
        )

class Default_Checkbox(ctk.CTkCheckBox):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(
            text_color = TEXT,
            font = BODY_FONT,
            onvalue = True,
            offvalue = False,
            checkbox_height = 20,
            checkbox_width = 20,
            border_color = TEXT,
            border_width = 2
        )

class Default_DateTime_Widget(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(
            text_color = TEXT,
            font = MICRO_FONT,
            corner_radius = 10,
            anchor = "center",
            height = 20,
            width = 75,
            fg_color = ENTRY_BACKGROUND,
            padx = 2
        )
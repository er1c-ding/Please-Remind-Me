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
reminder_count = 0
reminder_frames = []
reminders = []

class Default_Entry(ctk.CTkEntry):
    """Apply shared styling to text entries."""

    def __init__(self, master, **kwargs):
        """Configure entry colors, font, and alignment."""
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
    """Apply shared styling to labels."""

    def __init__(self, master, **kwargs):
        """Configure the label font and text color."""
        super().__init__(master, **kwargs)

        self.configure(
            text_color = TEXT,
            font = BODY_FONT
        )

class Default_Button(ctk.CTkButton):
    """Apply shared styling to standard buttons."""

    def __init__(self, master, **kwargs):
        """Configure the button colors, font, and alignment."""
        super().__init__(master, **kwargs)

        self.configure(
            fg_color = BUTTON,
            text_color = TEXT,
            font = BUTTON_FONT,
            anchor = "center"
        )

class Default_Little_Button(ctk.CTkButton):
    """Apply shared styling to compact action buttons."""

    def __init__(self, master, **kwargs):
        """Configure the compact button colors and font."""
        super().__init__(master, **kwargs)

        self.configure(
            fg_color = LITTLE_BUTTON,
            text_color = TEXT,
            font = BODY_FONT,
            anchor = "center"
        )

class Default_Save_Button(Default_Button):
    """Provide a standard SAVE button."""

    def __init__(self, master, **kwargs):
        """Set the save button label and dimensions."""
        super().__init__(master, **kwargs)

        self.configure(
            height = 40,
            width = 100,
            text = "SAVE"
        )

class Default_Title_Entry(Default_Entry):
    """Provide a styled reminder title input."""

    def __init__(self, master, **kwargs):
        """Set the title entry width and placeholder."""
        super().__init__(master, **kwargs)

        self.configure(
            width = 450,
            placeholder_text = "Enter Title Here"
        )

class Default_Checkbox(ctk.CTkCheckBox):
    """Provide a styled checkbox with boolean values."""

    def __init__(self, master, **kwargs):
        """Configure checkbox styling and toggle values."""
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
    """Display a date, time, or day label as a badge."""

    def __init__(self, master, **kwargs):
        """Configure the schedule badge appearance."""
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
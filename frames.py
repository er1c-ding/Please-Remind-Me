import customtkinter as ctk
import config

class Creation_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(
            height = 550,
            width = 500,
            fg_color = config.BACKGROUND
        )

class Recurring_Frame(Creation_Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure(3, weight=3)
        self.grid_columnconfigure(4, weight=12)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.information = ctk.CTkLabel(
            self,
            text = "This will repeatedly send a reminder at the interval \nspecified below.",
            text_color = config.TEXT,
            font = config.BODY_FONT,
            justify = "left"
        )

        self.information.grid(column = 0, row = 0, columnspan = 5, sticky = "w", padx = (20, 0))

        self.title_label = ctk.CTkLabel(
            self,
            text = "Title:",
            text_color = config.TEXT,
            font = config.BODY_FONT,            
        )
        
        self.title_label.grid(column = 0, row = 1, columnspan = 4, padx = (20, 0), sticky = "w", pady = (20, 0))

        self.title_entry = ctk.CTkEntry(
            self,
            font = config.BODY_FONT,
            width = 450,
            fg_color = config.ENTRY_BACKGROUND,
            text_color = config.TEXT,
            placeholder_text = "Enter Title Here",
            placeholder_text_color = config.PLACEHOLDER_TEXT,
            border_width = 0,
            justify = "center"
        )

        self.title_entry.grid(column = 0, row = 2, columnspan = 5, padx = (20, 0), sticky = "w", pady = (10, 0))

        self.specify_label = ctk.CTkLabel(
            self,
            text = "Specify Interval:",
            text_color = config.TEXT,
            font = config.BODY_FONT,            
        )
        
        self.specify_label.grid(column = 0, row = 3, columnspan = 5, padx = (20, 0), sticky = "w", pady = (20, 0))

        self.hours = ctk.CTkEntry(
            self,
            font = config.BODY_FONT,
            width = 50,
            fg_color = config.ENTRY_BACKGROUND,
            text_color = config.TEXT,
            placeholder_text = "HH",
            placeholder_text_color = config.PLACEHOLDER_TEXT,
            border_width = 0,
            justify = "center"
        )

        self.hours.grid(column = 0, row = 4, pady = (10, 0), sticky = "w", padx = (20, 0))

        self.colon = ctk.CTkLabel(
            self,
            text = ":",
            text_color = config.TEXT,
            font = config.BODY_FONT,            
        )
        
        self.colon.grid(column = 0, row = 4, sticky = "e", padx = (0, 5), pady = (10, 0))

        self.minutes = ctk.CTkEntry(
            self,
            font = config.BODY_FONT,
            width = 50,
            fg_color = config.ENTRY_BACKGROUND,
            text_color = config.TEXT,
            placeholder_text = "MM",
            placeholder_text_color = config.PLACEHOLDER_TEXT,
            border_width = 0,
            justify = "center"
        )

        self.minutes.grid(column = 1, row = 4, pady = (10, 0), sticky = "w")

        self.colon = ctk.CTkLabel(
            self,
            text = ":",
            text_color = config.TEXT,
            font = config.BODY_FONT,            
        )
        
        self.colon.grid(column = 1, row = 4, sticky = "e", padx = (0, 5), pady = (10, 0))

        self.seconds = ctk.CTkEntry(
            self,
            font = config.BODY_FONT,
            width = 50,
            fg_color = config.ENTRY_BACKGROUND,
            text_color = config.TEXT,
            placeholder_text = "SS",
            placeholder_text_color = config.PLACEHOLDER_TEXT,
            border_width = 0,
            justify = "center"
        )

        self.seconds.grid(column = 2, row = 4, pady = (10, 0), sticky = "w")

        self.save_button = ctk.CTkButton(
            self,
            width = 100,
            height = 40,
            text = "SAVE",
            anchor = "center",
            fg_color = config.BUTTON,
            text_color = config.TEXT,
            font = config.BUTTON_FONT,
        )

        self.save_button.grid(column = 0, row = 5, columnspan = 5, sticky = "w", padx = (20, 0), pady = (30,0))

class Daily_Frame(Creation_Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class One_Time_Frame(Creation_Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure(3, weight=3)
        self.grid_columnconfigure(4, weight=12)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        self.information = ctk.CTkLabel(
            self,
            text = "This will send a single reminder at the time and date \nspecified below.",
            text_color = config.TEXT,
            font = config.BODY_FONT,
            justify = "left"
        )

        self.information.grid(column = 0, row = 0, columnspan = 5, sticky = "w", padx = (20, 0))

        self.title_label = ctk.CTkLabel(
            self,
            text = "Title:",
            text_color = config.TEXT,
            font = config.BODY_FONT,            
        )
        
        self.title_label.grid(column = 0, row = 1, columnspan = 4, padx = (20, 0), sticky = "w", pady = (20, 0))

        self.title_entry = ctk.CTkEntry(
            self,
            font = config.BODY_FONT,
            width = 450,
            fg_color = config.ENTRY_BACKGROUND,
            text_color = config.TEXT,
            placeholder_text = "Enter Title Here",
            placeholder_text_color = config.PLACEHOLDER_TEXT,
            border_width = 0,
            justify = "center"
        )

        self.title_entry.grid(column = 0, row = 2, columnspan = 5, padx = (20, 0), sticky = "w", pady = (10, 0))

        self.specify_label = ctk.CTkLabel(
            self,
            text = "Specify Time:",
            text_color = config.TEXT,
            font = config.BODY_FONT,            
        )
        
        self.specify_label.grid(column = 0, row = 3, columnspan = 5, padx = (20, 0), sticky = "w", pady = (20, 0))

        self.hours = ctk.CTkEntry(
            self,
            font = config.BODY_FONT,
            width = 50,
            fg_color = config.ENTRY_BACKGROUND,
            text_color = config.TEXT,
            placeholder_text = "HH",
            placeholder_text_color = config.PLACEHOLDER_TEXT,
            border_width = 0,
            justify = "center"
        )

        self.hours.grid(column = 0, row = 4, pady = (10, 0), sticky = "w", padx = (20, 0))

        self.colon = ctk.CTkLabel(
            self,
            text = ":",
            text_color = config.TEXT,
            font = config.BODY_FONT,            
        )
        
        self.colon.grid(column = 0, row = 4, sticky = "e", padx = (0, 5), pady = (10, 0))

        self.minutes = ctk.CTkEntry(
            self,
            font = config.BODY_FONT,
            width = 50,
            fg_color = config.ENTRY_BACKGROUND,
            text_color = config.TEXT,
            placeholder_text = "MM",
            placeholder_text_color = config.PLACEHOLDER_TEXT,
            border_width = 0,
            justify = "center"
        )

        self.minutes.grid(column = 1, row = 4, pady = (10, 0), sticky = "w")

        self.colon = ctk.CTkLabel(
            self,
            text = ":",
            text_color = config.TEXT,
            font = config.BODY_FONT,            
        )
        
        self.colon.grid(column = 1, row = 4, sticky = "e", padx = (0, 5), pady = (10, 0))

        self.seconds = ctk.CTkEntry(
            self,
            font = config.BODY_FONT,
            width = 50,
            fg_color = config.ENTRY_BACKGROUND,
            text_color = config.TEXT,
            placeholder_text = "SS",
            placeholder_text_color = config.PLACEHOLDER_TEXT,
            border_width = 0,
            justify = "center"
        )

        self.seconds.grid(column = 2, row = 4, pady = (10, 0), sticky = "w")

        self.specify_label = ctk.CTkLabel(
            self,
            text = "Specify Date:",
            text_color = config.TEXT,
            font = config.BODY_FONT,            
        )
        
        self.specify_label.grid(column = 0, row = 5, columnspan = 5, padx = (20, 0), sticky = "w", pady = (20, 0))

        self.day = ctk.CTkEntry(
            self,
            font = config.BODY_FONT,
            width = 50,
            fg_color = config.ENTRY_BACKGROUND,
            text_color = config.TEXT,
            placeholder_text = "DD",
            placeholder_text_color = config.PLACEHOLDER_TEXT,
            border_width = 0,
            justify = "center"
        )

        self.day.grid(column = 0, row = 6, pady = (10, 0), sticky = "w", padx = (20, 0))

        self.slash = ctk.CTkLabel(
            self,
            text = "/",
            text_color = config.TEXT,
            font = config.BODY_FONT,            
        )
        
        self.slash.grid(column = 0, row = 6, sticky = "e", padx = (0, 5), pady = (10, 0))

        self.month = ctk.CTkEntry(
            self,
            font = config.BODY_FONT,
            width = 50,
            fg_color = config.ENTRY_BACKGROUND,
            text_color = config.TEXT,
            placeholder_text = "MM",
            placeholder_text_color = config.PLACEHOLDER_TEXT,
            border_width = 0,
            justify = "center"
        )

        self.month.grid(column = 1, row = 6, pady = (10, 0), sticky = "w")

        self.slash = ctk.CTkLabel(
            self,
            text = "/",
            text_color = config.TEXT,
            font = config.BODY_FONT,            
        )
        
        self.slash.grid(column = 1, row = 6, sticky = "e", padx = (0, 5), pady = (10, 0))

        self.year = ctk.CTkEntry(
            self,
            font = config.BODY_FONT,
            width = 75,
            fg_color = config.ENTRY_BACKGROUND,
            text_color = config.TEXT,
            placeholder_text = "YYYY",
            placeholder_text_color = config.PLACEHOLDER_TEXT,
            border_width = 0,
            justify = "center"
        )

        self.year.grid(column = 2, row = 6, pady = (10, 0), sticky = "w")

        self.save_button = ctk.CTkButton(
            self,
            width = 100,
            height = 40,
            text = "SAVE",
            anchor = "center",
            fg_color = config.BUTTON,
            text_color = config.TEXT,
            font = config.BODY_FONT,
        )

        self.save_button.grid(column = 0, row = 7, columnspan = 5, sticky = "w", padx = (20, 0), pady = (30,0))

class Default_Frame(Creation_Frame):
    def __init__(self, master, type, **kwargs):
        super().__init__(master, **kwargs)

        self.information = ctk.CTkLabel(
            self,
            text = f"You have chosen the default: \"{type}\"",
            text_color = config.TEXT,
            font = config.BODY_FONT
        )

        self.information.pack(anchor = "w", padx = (20, 0))

        self.save_button = ctk.CTkButton(
            self,
            width = 100,
            height = 40,
            text = "SAVE",
            anchor = "center",
            fg_color = config.BUTTON,
            text_color = config.TEXT,
            font = config.BODY_FONT,
        )

        self.save_button.pack(anchor = "w", padx = (20, 0), pady = (30,0))
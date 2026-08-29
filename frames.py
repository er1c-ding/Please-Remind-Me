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

        self.information = config.Default_Label(
            self,
            text = "This will repeatedly send a reminder at the interval \nspecified below.",
            justify = "left"
        )

        self.information.grid(column = 0, row = 0, columnspan = 5, sticky = "w", padx = (20, 0))

        self.title_label = config.Default_Label(
            self,
            text = "Title:"          
        )
        
        self.title_label.grid(column = 0, row = 1, columnspan = 4, padx = (20, 0), sticky = "w", pady = (20, 0))

        self.title_entry = config.Default_Title_Entry(
            self
        )

        self.title_entry.grid(column = 0, row = 2, columnspan = 5, padx = (20, 0), sticky = "w", pady = (10, 0))

        self.specify_label = config.Default_Label(
            self,
            text = "Specify Interval:"           
        )
        
        self.specify_label.grid(column = 0, row = 3, columnspan = 5, padx = (20, 0), sticky = "w", pady = (20, 0))

        self.hours = config.Default_Entry(
            self,
            width = 50,
            placeholder_text = "HH"
        )

        self.hours.grid(column = 0, row = 4, pady = (10, 0), sticky = "w", padx = (20, 0))

        self.colon = config.Default_Label(
            self,
            text = ":"          
        )
        
        self.colon.grid(column = 0, row = 4, sticky = "e", padx = (0, 5), pady = (10, 0))

        self.minutes = config.Default_Entry(
            self,
            width = 50,
            placeholder_text = "MM"
        )

        self.minutes.grid(column = 1, row = 4, pady = (10, 0), sticky = "w")

        self.colon = config.Default_Label(
            self,
            text = ":"          
        )
        
        self.colon.grid(column = 1, row = 4, sticky = "e", padx = (0, 5), pady = (10, 0))

        self.seconds = config.Default_Entry(
            self,
            width = 50,
            placeholder_text = "SS"
        )

        self.seconds.grid(column = 2, row = 4, pady = (10, 0), sticky = "w")

        self.save_button = config.Default_Save_Button(
            self
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

        self.information = config.Default_Label(
            self,
            text = "This will send a single reminder at the time and date \nspecified below.",
            justify = "left"
        )

        self.information.grid(column = 0, row = 0, columnspan = 5, sticky = "w", padx = (20, 0))

        self.title_label = config.Default_Label(
            self,
            text = "Title:"            
        )
        
        self.title_label.grid(column = 0, row = 1, columnspan = 4, padx = (20, 0), sticky = "w", pady = (20, 0))

        self.title_entry = config.Default_Title_Entry(
            self
        )

        self.title_entry.grid(column = 0, row = 2, columnspan = 5, padx = (20, 0), sticky = "w", pady = (10, 0))

        self.specify_label = config.Default_Label(
            self,
            text = "Specify Time:"
        )
        
        self.specify_label.grid(column = 0, row = 3, columnspan = 5, padx = (20, 0), sticky = "w", pady = (20, 0))

        self.hours = config.Default_Entry(
            self,
            width = 50,
            placeholder_text = "HH"
        )

        self.hours.grid(column = 0, row = 4, pady = (10, 0), sticky = "w", padx = (20, 0))

        self.colon = config.Default_Label(
            self,
            text = ":"
        )
        
        self.colon.grid(column = 0, row = 4, sticky = "e", padx = (0, 5), pady = (10, 0))

        self.minutes = config.Default_Entry(
            self,
            width = 50,
            placeholder_text = "MM"
        )

        self.minutes.grid(column = 1, row = 4, pady = (10, 0), sticky = "w")

        self.colon = config.Default_Label(
            self,
            text = ":"
        )
        
        self.colon.grid(column = 1, row = 4, sticky = "e", padx = (0, 5), pady = (10, 0))

        self.seconds = config.Default_Entry(
            self,
            width = 50,
            placeholder_text = "SS"
        )

        self.seconds.grid(column = 2, row = 4, pady = (10, 0), sticky = "w")

        self.specify_label = config.Default_Label(
            self,
            text = "Specify Date:"
        )
        
        self.specify_label.grid(column = 0, row = 5, columnspan = 5, padx = (20, 0), sticky = "w", pady = (20, 0))

        self.day = config.Default_Entry(
            self,
            width = 50,
            placeholder_text = "DD"
        )

        self.day.grid(column = 0, row = 6, pady = (10, 0), sticky = "w", padx = (20, 0))

        self.slash = config.Default_Label(
            self,
            text = "/"
        )
        
        self.slash.grid(column = 0, row = 6, sticky = "e", padx = (0, 5), pady = (10, 0))

        self.month = config.Default_Entry(
            self,
            width = 50,
            placeholder_text = "MM"
        )

        self.month.grid(column = 1, row = 6, pady = (10, 0), sticky = "w")

        self.slash = config.Default_Label(
            self,
            text = "/"
        )
        
        self.slash.grid(column = 1, row = 6, sticky = "e", padx = (0, 5), pady = (10, 0))

        self.year = config.Default_Entry(
            self,
            width = 75,
            placeholder_text = "YYYY"
        )

        self.year.grid(column = 2, row = 6, pady = (10, 0), sticky = "w")

        self.save_button = config.Default_Save_Button(
            self
        )

        self.save_button.grid(column = 0, row = 7, columnspan = 5, sticky = "w", padx = (20, 0), pady = (30,0))

class Default_Frame(Creation_Frame):
    def __init__(self, master, type, **kwargs):
        super().__init__(master, **kwargs)

        self.information = config.Default_Label(
            self,
            text = f"You have chosen the default: \"{type}\""
        )

        self.information.pack(anchor = "w", padx = (20, 0))

        self.save_button = config.Default_Save_Button(
            self
        )

        self.save_button.pack(anchor = "w", padx = (20, 0), pady = (30,0))
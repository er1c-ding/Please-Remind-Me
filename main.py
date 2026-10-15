import database
import gui
import timer

database.initialize_database()

app = gui.App()
my_timer = timer.Timer(app)
my_timer.start_timer()

database.load_reminders_from_database(app)

app.mainloop()

import database
import gui
import timer

database.initialize_database()

app = gui.App()
my_timer = timer.Timer(app)
my_timer.start_timer()
app.mainloop()

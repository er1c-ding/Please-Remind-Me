import gui
import timer

app = gui.App()
my_timer = timer.Timer(app)
my_timer.start_timer()
app.mainloop()
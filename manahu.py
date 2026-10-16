import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk 

class Main(Gtk.ApplicationWindow):
    def __init__(self, **kargs):
        super().__init__(**kargs, title="Manahu-Term")
        self.button = Gtk.Button(label="Click Me!!")
        self.button.connect("clicked", self.on_button_clicked)
        self.set_child(self.button)

    def on_button_clicked(self, _widget):
        self.close()

def on_activate(app):
    #create ApplicationWindow
    Window = Main(application=app)
    Window.present()

app = Gtk.Application(application_id="com.manahu-Term.Terminal")
app.connect("activate", on_activate)

app.run(None)





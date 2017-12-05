import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject


class MyWindow(Gtk.Window):

    def startTimer(self, widget):
        t1 = self.time.get_text()
        self.timer.start_odliczania(int(t1) - 1)

    def startTimer1(self, widget):
        t1 = 5 * 50
        self.timer.start_odliczania(int(t1) - 1)

    def startTimer2(self, widget):
        t1 = 8 * 60
        self.timer.start_odliczania(int(t1) - 1)

    def startTimer3(self, widget):
        t1 = 2 * 60
        self.timer.start_odliczania(int(t1) - 1)

    def startTimer4(self, widget):
        t1 = 30
        self.timer.start_odliczania(int(t1) - 1)

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.box2 = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box2)
        self.box = Gtk.Box(spacing=6)
        self.box2.pack_start(self.box, True, True, 0)
        self.box3 = Gtk.Box(spacing=6)
        self.box2.pack_start(self.box3, True, True, 0)

        self.button1 = Gtk.Button(label="Jajka (5')")
        self.button1.connect("clicked", self.startTimer1)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Makaron (8')")
        self.button2.connect("clicked", self.startTimer2)
        self.box.pack_start(self.button2, True, True, 0)

        self.button3 = Gtk.Button(label="Stek (2')")
        self.button3.connect("clicked", self.startTimer3)
        self.box3.pack_start(self.button3, True, True, 0)

        self.button4 = Gtk.Button(label="Tortilla (30'')")
        self.button4.connect("clicked", self.startTimer4)
        self.box3.pack_start(self.button4, True, True, 0)

        self.time = Gtk.Entry()
        # self.time.set_text("czas")
        self.time.connect("activate", self.startTimer)
        self.box2.pack_start(self.time, True, True, 0)

        self.timer = Odliczanie()
        self.box2.pack_start(self.timer, True, True, 0)


class Odliczanie(Gtk.Label):
    def __init__(self):
        Gtk.Label.__init__(self)
        self.time = 0

    def countdown(self):
        if self.time > 0:
            self.set_text(str(self.time))
            self.time -= 1
            return True
        else:
            self.time = 0
            self.set_text(str(self.time))
            return False

    def start_odliczania(self, time):
        self.time = time
        self.id = GObject.timeout_add(1000, self.countdown)


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

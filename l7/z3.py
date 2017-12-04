#!/usr/bin/env python
# clock_ex1.py

import gtk

class EggClockFace(gtk.DrawingArea):
    def __init__(self):
        gtk.DrawingArea.__init__(self)
        self.connect("expose_event", self.expose)
        
    def expose(self, widget, event):
        return False

def main():
    window = gtk.Window()
    clock = EggClockFace()
    
    window.add(clock)
    window.connect("destroy", gtk.main_quit)
    window.show_all()
    
    gtk.main()
    
if __name__ == "__main__":
    main()


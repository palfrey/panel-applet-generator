#!/usr/bin/python

import sys
from gi.repository import Gtk
from gi.repository import PanelApplet

def applet_factory(applet, iid, data = None):
	button = Gtk.Button("It works!")
	applet.add(button)
	applet.show_all()
	return True
				
if __name__ == '__main__':	# testing for execution
	print('Starting factory')

	if len(sys.argv) > 1 and sys.argv[1] == '-d': # debugging
		mainWindow = Gtk.Window()
		mainWindow.set_title('Applet window')
		mainWindow.connect('destroy', Gtk.main_quit)
		applet_factory(mainWindow, None)
		mainWindow.show_all()
		Gtk.main()
		sys.exit()
	else:
		PanelApplet.Applet.factory_main("TimetrackerWidgetFactory", PanelApplet.Applet.__gtype__, applet_factory, None)

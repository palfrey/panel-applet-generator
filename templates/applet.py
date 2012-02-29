try:
	from gi.repository import Gtk
except: # Can't use ImportError, as gi.repository isn't quite that nice...
	import gtk as Gtk

def applet_factory(applet, iid, data = None):
	button = Gtk.Button("It works!")
	applet.add(button)
	applet.show_all()
	return True

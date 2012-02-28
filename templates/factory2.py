#!/usr/bin/python

import sys
import gtk
import pygtk
pygtk.require('2.0')
import gnomeapplet
from ${name}Applet import applet_factory

if __name__ == '__main__':	 # testing for execution
	print('Starting factory')

	if len(sys.argv) > 1 and sys.argv[1] == '-d': # debugging
		mainWindow = gtk.Window()
		mainWindow.set_title('Applet window')
		mainWindow.connect('destroy', gtk.main_quit)
		applet = gnomeapplet.Applet()
		applet_factory(applet, None)
		applet.reparent(mainWindow)
		mainWindow.show_all()
		gtk.main()
		sys.exit()
	else:
		gnomeapplet.bonobo_factory('OAFIID:${name}_Factory', 
				gnomeapplet.Applet.__gtype__, 
				'${name}',
				'0.1', 
				applet_factory)

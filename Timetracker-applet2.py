#!/usr/bin/python

import sys
import gtk
import pygtk
import gnomeapplet

pygtk.require('2.0')

def applet_factory(applet, iid):
	button = gtk.Button("It works!")
	applet.add(button)
	applet.show_all()
	return True
            
if __name__ == '__main__':   # testing for execution
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
      gnomeapplet.bonobo_factory('OAFIID:TimetrackerApplet_Factory', 
                                 gnomeapplet.Applet.__gtype__, 
                                 'Timetracker', '0.1', 
                                 applet_factory)

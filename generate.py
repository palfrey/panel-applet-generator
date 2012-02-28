from genshi.template.text import NewTextTemplate
from os import getenv, makedirs, walk, stat, chmod
from os.path import exists, join, dirname
from time import strftime, gmtime

name = "HelloWorld"
description = "Timetracker applet"
icon = "time-admin.png"
category = "Utility"
scriptRoot = "/usr/lib/gnome-applets/"
#parser.add_option("-n","--name",dest="name",default=getenv("debfullname","default name"), help="Maintainer name (Default: %s)"%getenv("DEBFULLNAME","Default name"))
maintainer = getenv("debfullname","default name")
#parser.add_option("-e","--email",dest="email",default=getenv("DEBEMAIL","fixme@invalid_email_path"),help="Maintainer email (Default: %s)"%getenv("DEBEMAIL","fixme@invalid_email_path"))
email = getenv("DEBEMAIL","fixme@invalid_email_path")
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
folder = name

templates = [
		("applet.py", "%sApplet.py" % name),
		("bonobo-server.template", "%s.server" % name),
		("dbus-service.template", "org.gnome.panel.applet.%s.service" % name),
		("factory2.py", "%s-factory2.py" % name),
		("factory3.py", "%s-factory3.py" % name),
		("panel-applet.template", "org.gnome.applets.%s.panel-applet" % name),
		]

for root,dirs,files in walk("templates/debian"):
	for f in files:
		fullpath = join(root,f)[len("templates/"):]
		templates.append((fullpath, fullpath))

for (src, dest) in templates:
	src = join("templates", src)
	dest = join(folder, dest)
	destdir = dirname(dest)
	if destdir != "" and not exists(destdir):
		makedirs(destdir)
	tmpl = NewTextTemplate(open(src).read())
	stream = tmpl.generate(
			name = name,
			scriptRoot = scriptRoot,
			description = description,
			icon = icon,
			category = category,
			lowerName = name.lower(),
			maintainer = maintainer,
			email = email,
			now = now)
	open(dest, "wb").write(stream.render())

	bits = stat(src).st_mode
	chmod(dest, bits)

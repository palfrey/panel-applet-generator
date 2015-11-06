#!/usr/bin/python

from genshi.template.text import NewTextTemplate
from os import getenv, makedirs, walk, stat, chmod
from os.path import exists, join, dirname
from time import strftime, gmtime
from optparse import OptionParser

parser = OptionParser(description="Panel applet generator")

parser.add_option("-n", "--name", dest="name", help="Applet name (required)", default=None)
parser.add_option("-d", "--description", dest="description", help="Description (required)", default=None)
parser.add_option("-i", "--icon", dest="icon", default= "time-admin.png", help="Icon (in /usr/share/icons, without the full path)")
parser.add_option("-c", "--category", dest="category", help="Category of the applet (see http://standards.freedesktop.org/menu-spec/latest/apa.html for full list)", default = "Utility")
parser.add_option("--maintainer",dest="maintainer",default=getenv("debfullname","default name"), help="Maintainer name (Default: %s)"%getenv("DEBFULLNAME","Default name"))
parser.add_option("-e","--email",dest="email",default=getenv("DEBEMAIL","fixme@invalid_email_path"),help="Maintainer email (Default: %s)"%getenv("DEBEMAIL","fixme@invalid_email_path"))
parser.add_option("-f", "--folder", help="Destination folder (default: same as the name)", dest="folder", default=None)

(opts, args) = parser.parse_args()
if args != []:
	parser.error("Extra arguments after named parameters! %s"%(",".join(args)))
if opts.name == None:
	parser.error("Need a name for the applet!")
if opts.description == None:
	parser.error("Need a description for the applet!")

name = opts.name
if opts.folder == None:
	opts.folder = name
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
scriptRoot = "/usr/lib/gnome-applets"

templates = [
		("applet.py", "%sApplet.py" % name),
		("bonobo-server.template", "%s.server" % name),
		("mate-server.template", "%s-mate.server" % name),
		("dbus-service.template", "org.gnome.panel.applet.%s.service" % name),
		("factory2.py", "%s-factory2.py" % name),
		("factory3.py", "%s-factory3.py" % name),
		("factoryMate.py", "%s-factoryMate.py" % name),
		("panel-applet.template", "org.gnome.applets.%s.panel-applet" % name),
		]

for root,dirs,files in walk("templates/debian"):
	for f in files:
		fullpath = join(root,f)[len("templates/"):]
		templates.append((fullpath, fullpath))

for (src, dest) in templates:
	src = join("templates", src)
	dest = join(opts.folder, dest)
	destdir = dirname(dest)
	if destdir != "" and not exists(destdir):
		makedirs(destdir)
	tmpl = NewTextTemplate(open(src).read())
	stream = tmpl.generate(
			name = opts.name,
			scriptRoot = scriptRoot,
			description = opts.description,
			icon = opts.icon,
			category = opts.category,
			lowerName = opts.name.lower(),
			maintainer = opts.maintainer,
			email = opts.email,
			now = now)
	open(dest, "wb").write(stream.render())

	bits = stat(src).st_mode
	chmod(dest, bits)

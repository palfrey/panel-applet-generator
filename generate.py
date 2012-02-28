from genshi.template import TemplateLoader
from genshi.template.text import NewTextTemplate

name = "Timetracker"
description = "Timetracker applet"
icon = "time-admin.png"
category = "Utility"
path = "/home/palfrey/src/timetracker-widget/applet.py"

templates = [
		("applet.py", "%sApplet.py" % name),
		("bonobo-server.template", "%s.server" % name),
		("dbus-service.template", "org.gnome.panel.applet.%s.service" % name),
		("factory2.py", "%s-factory2.py" % name),
		("factory3.py", "%s-factory3.py" % name),
		("panel-applet.template", "org.gnome.applets.%s.panel-applet" % name)
		]

loader = TemplateLoader("templates")

for (src, dest) in templates:
	tmpl = loader.load(src, cls=NewTextTemplate)
	stream = tmpl.generate(name=name, path=path, description=description, icon=icon, category=category)
	open(dest, "wb").write(stream.render())

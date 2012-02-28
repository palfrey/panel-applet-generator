panel-applet-generator
-----------------------
Makes all the basic boilerplate for applets that are compatible with both 2.x and 3.x Gnome panels.

Usage: panel-applet-generator.py [options]

Options:
  -h, --help            show this help message and exit
  -n NAME, --name=NAME  Applet name (required)
  -d DESCRIPTION, --description=DESCRIPTION
                        Description (required)
  -i ICON, --icon=ICON  Icon (in /usr/share/icons, without the full path)
  -c CATEGORY, --category=CATEGORY
                        Category of the applet (see
                        http://standards.freedesktop.org/menu-
                        spec/latest/apa.html for full list)
  --maintainer=MAINTAINER
                        Maintainer name
  -e EMAIL, --email=EMAIL
                        Maintainer email
  -f FOLDER, --folder=FOLDER
                        Destination folder (default: same as the name)

You'll need at least a name and description, but filling in the rest is a good idea

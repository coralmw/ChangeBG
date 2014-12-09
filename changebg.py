import PIL.Image as Image
from gi.repository import Gio, GLib
import sys

SCHEMA = 'org.gnome.desktop.background'
FPATH = '/home/tparks/bg.png'
l = Image.open(sys.argv[1])
r = Image.open(sys.argv[2])

l = l.resize((2560, 1440), Image.ANTIALIAS)
r = r.resize((2560, 1440), Image.ANTIALIAS)
singlewidth = 2560
height = 1440
width = singlewidth*2
out = Image.new('RGB', (width, height))
out.paste(l, (0, 0, singlewidth, height))
out.paste(r, (singlewidth, 0, singlewidth*2, height))

BGsettings = Gio.Settings.new(SCHEMA)

out.save(FPATH)
BGsettings.set_value('picture-uri', GLib.Variant.new_string(FPATH))
BGsettings.set_value('picture-options', GLib.Variant.new_string('spanned'))

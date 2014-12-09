import PIL as Image
import sys

l = Image.open(sys.arg[2])
l = Image.open(sys.arg[3])

l = l.resize((2560, 1440), Image.ANTIALIAS)
r = r.resize((2560, 1440), Image.ANTIALIAS)
singlewidth = 2560
height = 1440
width = singlewidth*2
out = Image.new('RGB', (width, height))
out.paste(l, (0, 0, singlewidth, height))
out.paste(r, (singlewidth, 0, singlewidth*2, height))

out.save('joined.png')

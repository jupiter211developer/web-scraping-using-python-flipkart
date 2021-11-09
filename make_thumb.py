import glob
from PIL import Image

for infile in glob.glob('logo.png'):
    img = Image.open(infile)
    img.thumbnail((128, 128), Image.ANTIALIAS)
    img.save('thumb_' + infile, 'png')

print('make thumbnail image')
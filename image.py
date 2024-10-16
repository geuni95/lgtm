import os
from PIL import Image

def thumbnail(infile, size=(128, 128)):
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    try:
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(outfile, "JPEG")
    except IOError:
        print("cannot create thumbnail for", infile)

if __name__ == "__main__":
    thumbnail(r'C:\workspace\fulfillPython-main\fulfillPython-main\13-application\dog.jpg')
    
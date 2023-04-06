# Script converts .tga files to .png format from given path
# developed by ksiazeblaznow

from asyncio.windows_events import NULL
from PIL import Image
import os
import sys


if len(sys.argv) > 1:
    print("Export from path: /" + sys.argv[1])
    print("...to path:       /" + sys.argv[2])

    # code:
    files = os.listdir(sys.argv[1])
    print(files)

    for file in files:
        pngFilename = file[:-4] + ".png"
        Image.open(sys.argv[1] + "/" + file).save(sys.argv[2] + "/" + pngFilename)

    print('Success :))')

else:
    print("Invalid arguments: set export paths in .bat file")
#!/usr/bin/env python

import os
import PIL
from PIL import Image

SUFFIX = '_s'
WIDTH = 670
HEIGHT = 335

for file in os.listdir('.'):

    name, extension = os.path.splitext(file)
    targetName = name + SUFFIX + extension

    if extension == '.png' and not name.endswith(SUFFIX) and not (os.path.isfile(targetName)):

        print("creating file '" + targetName + "' from '" + file + "'.")

        img = Image.open(file)
        img = img.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        img.save(targetName)

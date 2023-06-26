import os
from PIL import Image, ImageSequence
import sys
import math
import numpy as np

# CONFIG 
brightness = ' .-=;?#%@'
# Fun fact: with a width of 14 in Windows (15 in linux)
# the ASCII Art persists in a Hex dump of the file
# 14 because the width is 16 and linebreaks take 2 chars 
# in Windows (\r\n) and 1 char in unix (\n)
WIDTH_OUT = 14
ADD_SPACES = False
filename = 'heart4.png'
TRIM_SIDE_COLS_IF_EMPTY = True

# Load and convert to BW
image = Image.open(filename)
image = image.convert("L")

# Resize
width, height = image.size
if width > WIDTH_OUT :
    HEIGHT_OUT = int(round((WIDTH_OUT / width) * height))
    # Vertically compress if we don't add spaces to keep dimensions acceptable
    if ADD_SPACES == False :
        HEIGHT_OUT = round(0.5 * HEIGHT_OUT)
    image = image.resize((WIDTH_OUT, HEIGHT_OUT), Image.BICUBIC)

# Convert to list
image = list(image.getdata())

# Normalize 
(b_min, b_max) = (min(image), max(image))
b_span = b_max - b_min
fn_normalize = lambda b: (b - b_min) / b_span
image_norm = [(b - b_min) / b_span for b in image]

# Convert to ASCII
image_ascii = [(brightness[math.floor(x * (len(brightness)-1))] + (' ' if ADD_SPACES else '')) for x in image_norm]

# Split lines
ascii_out = ''
i = 0
while i < len(image_ascii) :
    if i % WIDTH_OUT == 0 and i > 0:
        ascii_out += '\n'
    ascii_out += image_ascii[i]
    i += 1

# Print result
# print(ascii_out)

outfile = open(filename.split('.')[0] + ".txt", "w")
outfile.write(ascii_out)
outfile.flush()
outfile.close()

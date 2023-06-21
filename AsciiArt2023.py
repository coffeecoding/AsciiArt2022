import os
from PIL import Image, ImageSequence
import sys
import math
import numpy as np

brightness = ' .-=;?#%@'

# CONFIG (DIMENSIONS)
WIDTH_OUT = 32           

filename = 'img.png'

# Load and convert to BW
image = Image.open(filename)
image = image.convert("L")

# Resize
width, height = image.size
if width > WIDTH_OUT :
    HEIGHT_OUT = int(round((WIDTH_OUT / width) * height))
    image = image.resize((WIDTH_OUT, HEIGHT_OUT), Image.BICUBIC)

# Convert to list
image = list(image.getdata())

# Normalize 
(b_min, b_max) = (min(image), max(image))
b_span = b_max - b_min
fn_normalize = lambda b: (b - b_min) / b_span
image_norm = [(b - b_min) / b_span for b in image]

# Convert to ASCII
image_ascii = [(brightness[math.floor(x * (len(brightness)-1))] + ' ') for x in image_norm]

# Split lines
ascii_out = ''
i = 0
while i < len(image_ascii) :
    if i % WIDTH_OUT == 0 and i > 0:
        ascii_out += '\n'
    ascii_out += image_ascii[i]
    i += 1

# Print result
print(ascii_out)


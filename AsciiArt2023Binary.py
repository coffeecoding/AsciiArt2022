import os
from PIL import Image, ImageSequence
import sys
import math
import numpy as np

# Binary version
# Open the output as a HexDump and watch in awe the Art

# CONFIG 
# Binary mode: we only use 'C' for black and '0' for white
# Since C is arguably the darkest Hex char, and 0 the lightest
# Width is always 16
filename = 'grl.jpg'
TRIM_SIDE_COLS_IF_EMPTY = True

# Load and convert to BW
image = Image.open(filename)
image = image.convert("L")

# Resize
width, height = image.size
if width > 16 :
    HEIGHT_OUT = int(round((16 / width) * height))
    # Vertically compress if we don't add spaces to keep dimensions acceptable
    HEIGHT_OUT = round(0.5 * HEIGHT_OUT)
    image = image.resize((16, HEIGHT_OUT), Image.BICUBIC)

# Convert to list
image = list(image.getdata())

# Normalize 
(b_min, b_max) = (min(image), max(image))
b_span = b_max - b_min
fn_normalize = lambda b: (b - b_min) / b_span
image_norm = [(b - b_min) / b_span for b in image]

# Convert to ASCII
output = [(b'\xCC' if x < 0.4 else b'\x00') for x in image_norm]
output_bytes = b''.join(output)

# Print result
# print(ascii_out)

outfile = open(filename.split('.')[0] + "_binary.txt", "wb")
outfile.write(output_bytes)
outfile.flush()
outfile.close()

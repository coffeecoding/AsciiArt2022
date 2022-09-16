import imageio
import sys
import math

# CONSTANTS
brightness = '@%#*+=:-. '   # 10 characters => get index by int((brightness / 256) * 10)     <--- this one looks best
length = len(brightness)
inputimage = 'inputimg'
img = imageio.imread(inputimage + '.png')
out = open(inputimage + ".txt", "w")

# NORMALIZE IMAGE
b_min = 255
b_max = 0
for row in img :
    for val in row :
        b = (0.299*val[0] + 0.587*val[1] + 0.114*val[2])      # luminance (perceived brightness): https://stackoverflow.com/a/596243/12213872
        if (b < b_min) :
            b_min = b 
        if (b > b_max) : 
            b_max = b
print(b_min)
print(b_max)
# normalization factor n
n = 255 / b_max
# scale all [r, g, b] with n: n*r, n*g, n*b
for row in img :
    for val in row :
        val[0] *= n
        val[1] *= n
        val[2] *= n

# sys.exit('exiting ...')

# CONVERT TO ASCII
for row in img :
    for val in row :
        b = 0.299*val[0] + 0.587*val[1] + 0.114*val[2]
        b_idx = math.floor(b / 255 * (length-1))
        out.write(brightness[b_idx] + ' ')
    out.write("\n")
out.close()
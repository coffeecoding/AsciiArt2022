import imageio
import sys
import math
import numpy as np

# CONSTANTS
brightness = '@%#*+=-. '   # 10 characters => get index by int((brightness / 256) * 10)     <--- this one looks best
brightness = ' .-=;?#%@'
length = len(brightness)
inputimage = 'img'
img = imageio.imread(inputimage + '.png')
out = open(inputimage + ".txt", "w")

aa = [[1, 1], [2, 2]]
print(aa)
fn_inner = lambda x: x + 1
fn_trivial = lambda row: [fn_inner(x) for x in row]
print(list(map(fn_trivial, aa)))

# 1. Map image to brightness map
b_map = np.zeros((img.shape[0], img.shape[1]))
print(b_map.shape)
fn_calc_b = lambda px: 0.299*px[0] + 0.587*px[1] + 0.114*px[2]      # luminance (perceived brightness): https://stackoverflow.com/a/596243/12213872
fn_apply_calc_b_to_row = lambda row: [fn_calc_b(x) for x in row]    # [a, b, ...] => [f(a), f(b), ...]
b_map = np.array(list(map(fn_apply_calc_b_to_row, img)))

# 2. Normalize brightness map
(b_min, b_max) = (b_map.min(), b_map.max())
print((b_min, b_max))
b_span = b_max - b_min
fn_normalize = lambda b: (b - b_min) / b_span
fn_normalize_row = lambda row: [fn_normalize(x) for x in row]
b_map_norm = np.array(list(map(fn_normalize_row, b_map)))
# print((b_map_norm.min(), b_map_norm.max()))                       # should be (0.0, 1.0) 

# CONVERT TO ASCII
for row in b_map_norm :
    for b in row :
        b_idx = math.floor(b * (length-1))
        out.write(brightness[b_idx] + ' ')
    out.write("\n")
out.close()

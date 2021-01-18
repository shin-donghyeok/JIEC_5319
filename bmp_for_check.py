"""
2019. 04. 12.
Donghyeok Shin
"""
from PIL import Image

"""##########################"""
row = 6
col = 1
base = 6
distance = 10
needle_height = 1000
layer_height = 10
"""##########################"""

width = col * base + (col - 1) * distance + 60
height = row * base + (row - 1) * distance + 60

file_number = 0
file_name = str(file_number).zfill(4) + '.bmp'
file_number = file_number + 1
im = Image.new("L", (width, height), 255)
im.save(file_name)

layer = (int)(needle_height / layer_height)
BASE = base
if BASE % 2 == 1:
    BASE = BASE + 1
BASE = (int)(BASE / 2) - 1
node = [0]
for i in range(1, BASE):
    node.append(i * (int)(layer/BASE))
node.append(layer)
print(node)

ineedle = Image.new("L", (base + 10, layer + 10), 0)
ineedle_raw = ineedle.load()

alpha = 0
for I in range(1, BASE + 1):
    K = 0
    for J in range(node[I-1], node[I]):
        print(J, alpha)
        im = Image.new("L", (width, height), 0)
        im_raw = im.load()

        GRAY = (int)(255 / (node[I] - node[I-1]))
        for i in range(0, row):
            if ((i + 1) % 3 == 0) or ((i + 1) % 3 == 2):
                for j in range(0, col):
                    x = 30 + i * (base + distance)
                    y = 30 + j * (base + distance)
                    for X in range(x + alpha, x + base - alpha):
                        ineedle_y = alpha
                        for Y in range(y + alpha, y + base - alpha):
                            im_raw[Y, X] = 255 - GRAY * K
                            ineedle_raw[ineedle_y + 5, J + 5] = 255 - GRAY * K
                            ineedle_y = ineedle_y + 1
                            """
            if (i + 1) % 3 == 2:
                for j in range(0, col):
                    x = 30 + i * (base + distance)
                    y = 30 + j * (base + distance)
                    for X in range(x + alpha, x + base - alpha):
                        for Y in range(y + alpha, y + base - alpha):
                            im_raw[Y, X] = 255
                            """
            if (i + 1) % 3 == 1:
                for j in range(0, col):
                    x = 30 + i * (base + distance)
                    y = 30 + j * (base + distance)
                    for X in range(x, x + base):
                        for Y in range(y, y + base):
                            im_raw[Y, X] = 255
        K = K + 1
        for i in range(0, row):
            """
            if (i + 1) % 3 == 0:
            """
            if ((i + 1) % 3 == 0) or ((i + 1) % 3 == 2):
                for j in range(0, col):
                    x = 30 + i * (base + distance)
                    y = 30 + j * (base + distance)
                    if alpha + 1 < base - alpha - 1:
                        for X in range(x + alpha + 1, x + base - alpha - 1):
                            ineedle_y = alpha + 1
                            for Y in range(y + alpha + 1, y + base - alpha - 1):
                                im_raw[Y, X] = 255
                                ineedle_raw[ineedle_y + 5, J + 5] = 255
                                ineedle_y = ineedle_y + 1

        file_name = str(file_number).zfill(4) + '.bmp'
        file_number = file_number + 1
        im.save(file_name)
    alpha = alpha + 1

for i in range(0, 5):
    im = Image.new("L", (width, height), 0)
    file_name = str(file_number).zfill(4) + '.bmp'
    file_number = file_number + 1
    im.save(file_name)

file_name = 'needle.bmp'
ineedle.save(file_name)

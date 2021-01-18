"""
2020. 03. 02.
Donghyeok Shin
"""
from PIL import Image

"""##########################"""
row = 15
col = 25
base = 6
distance = 10
needle_height = 1000
layer_height = 10
"""##########################"""

width = col * base + (col - 1) * distance + 70
height = row * base + (row - 1) * distance + 70

file_number = 0
for i in range(0, 5):
    im = Image.new("L", (width, height), 255)
    file_name = str(file_number).zfill(4) + '.bmp'
    file_number = file_number + 1
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

alpha = 0
for I in range(1, BASE + 1):
    K = 0
    for J in range(node[I-1], node[I]):
        """print(J, alpha)"""
        im = Image.new("L", (width, height), 0)
        im_raw = im.load()

        """y=-3.140 + 61.28x + 49.13x^2"""
        GRAY = (int)(255 / (node[I] - node[I-1]))
        for i in range(0, row):
            for j in range(0, col):
                x = 30 + i * (base + distance)
                y = 30 + j * (base + distance)
                for X in range(x + alpha, x + base - alpha):
                    for Y in range(y + alpha, y + base - alpha):
                        TEMP = (int)(256 * (pow(100 * (255 - GRAY * K) / 256 / 49 + 0.45, 0.5) - 0.62))
                        print(TEMP)
                        im_raw[Y, X] = TEMP
                        """im_raw[Y, X] = 255 - GRAY * K"""
        K = K + 1
        for i in range(0, row):
            for j in range(0, col):
                x = 30 + i * (base + distance)
                y = 30 + j * (base + distance)
                if alpha + 1 < base - alpha - 1:
                    for X in range(x + alpha + 1, x + base - alpha - 1):
                         for Y in range(y + alpha + 1, y + base - alpha - 1):
                            im_raw[Y, X] = 255

        file_name = str(file_number).zfill(4) + '.bmp'
        file_number = file_number + 1
        im.save(file_name)
    alpha = alpha + 1

for i in range(0, 5):
    im = Image.new("L", (width, height), 0)
    file_name = str(file_number).zfill(4) + '.bmp'
    file_number = file_number + 1
    im.save(file_name)

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

"""##########################"""
row = 20
col = 41
base = 6
distance = 10
needle_height = 1000
layer_height = 10
"""##########################"""

width = col * base + (col - 1) * distance + 60
height = row * base + (row - 1) * distance + 60

file_number = 0
for i in range(0, 3):
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



array_x = base
array_y = base
array_z = layer
filled = np.array([[[1]*array_z]*array_y]*array_x)
colors = np.empty(filled.shape, dtype=object)



alpha = 0
for I in range(1, BASE + 1):
    K = 0
    for J in range(node[I-1], node[I]):
        im = Image.new("L", (width, height), 0)
        im_raw = im.load()

        GRAY = (int)(255 / (node[I] - node[I-1]))
        for i in range(0, row):
            for j in range(0, col):
                if (i < 5 or i >= 15) and (j + 1) % 10 == 1:
                    x = 30 + i * (base + distance)
                    y = 30 + j * (base + distance)

                    for X in range(x, x + base):
                        for Y in range(y, y + base):
                            colors[X - x][Y - y][J] = [0, 0, 0]

                    for X in range(x + alpha, x + base - alpha):
                        for Y in range(y + alpha, y + base - alpha):
                            im_raw[Y, X] = 255 - GRAY * K
                            graycolor = (255 - GRAY * K) / 255
                            colors[X - x][Y - y][J] = [graycolor, graycolor, graycolor]
                            filled[X - x][Y - y][J] = 1
        K = K + 1
        for i in range(0, row):
            for j in range(0, col):
                if (i < 5 or i >= 15) and (j + 1) % 10 == 1:
                    x = 30 + i * (base + distance)
                    y = 30 + j * (base + distance)
                    if alpha + 1 < base - alpha - 1:
                        for X in range(x + alpha + 1, x + base - alpha - 1):
                            for Y in range(y + alpha + 1, y + base - alpha - 1):
                                im_raw[Y, X] = 255
                                colors[X - x][Y - y][J] = [1, 1, 1]
                                filled[X - x][Y - y][J] = 1

        file_name = str(file_number).zfill(4) + '.bmp'
        file_number = file_number + 1
        im.save(file_name)
    alpha = alpha + 1

for i in range(0, 5):
    im = Image.new("L", (width, height), 0)
    file_name = str(file_number).zfill(4) + '.bmp'
    file_number = file_number + 1
    im.save(file_name)

for i in range(0, 6):
    for j in range(0, 3):
        for k in range(0, layer):
            filled[i][j][k] = 0




def make_ax(grid=False):
    fig = plt.figure(figsize=(6, 10))
    ax = fig.gca(projection='3d', proj_type='ortho')  # 원근법
    ax.view_init(elev=10., azim=300)  # 시점변경
    ax.set_xlabel("x", size=20)
    ax.set_ylabel("y", size=20)
    ax.set_zlabel("z", size=20)
    ax.grid(grid)
    return ax

ax = make_ax(True)
ax.voxels(filled, facecolors=colors, edgecolors=[0.5, 0.5, 0.5], linewidth=0.5)
plt.show()

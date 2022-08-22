"""
Module to plot the Julia set (formula: `f(z) = z**2 + c`,
where `z` is a complex variable and `c` is a complex constant).
"""

import numpy as np
import matplotlib.pyplot as plt

from math import sqrt
from random import random
from matplotlib import colors

# Plot size in pixels
N, M = 1000, 1000

# Real and imaginary parts of C
CX, CY = -0.74543, 0.11301
# CX, CY = -0.75, 0.11
# CX, CY = -0.1, 0.651

# Radius: must be such that r**2 - r >= sqrt(cx**2 + cy**2)
radius = 0
while radius ** 2 - radius < sqrt(CX ** 2 + CY ** 2):
    radius += 0.1


def initplane(n, m, cx, cy, r):
    """Function to calculate the plane."""

    # Initializing plane
    plane = [[None] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            # scaling to be between -R and R
            zx = -r + i * (2 * r / n)
            zy = -r + j * (2 * r / m)

            iteration = 0
            max_iteration = 100

            # calculating next value
            while zx ** 2 + zy ** 2 < r ** 2 and iteration < max_iteration:
                xtemp = zx ** 2 - zy ** 2
                zy = 2 * zx * zy + cy
                zx = xtemp + cx
                iteration += 1

            plane[i][j] = iteration
    return plane


def add_white(colormap):
    # doesn't conflict with vstack
    black = plt.cm.binary(255)
    # 255 because 1 is taken by black
    colormap = colormap(np.linspace(0, 1, 255))
    # stack both together
    colormap = np.vstack((colormap, black))
    # cast to MPL colormap type
    return colors.LinearSegmentedColormap.from_list('my_colormap', colormap)


if __name__ == "__main__":
    plane = initplane(N, M, CX, CY, radius)
    cmap = add_white(plt.cm.viridis)
    plt.imsave(f"julia_normal_{N}x{M}_c={CX}{'+' if CY>0 else '-'}{abs(CY)}i.png",
           plane, cmap=cmap)

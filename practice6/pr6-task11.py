"""
Module to plot the Julia set (formula: `f(z) = z**2 + c`,
where `z` is a complex variable and `c` is a complex constant).
"""

import sys
from math import sqrt
from random import random

import matplotlib.pyplot as plt
from matplotlib import colors
from numpy import linspace, vstack


def initplane(n, m, cx, cy, r, max_iter, prog=True):
    """Function to calculate the plane."""

    # Initializing plane
    plane = [[None] * m for _ in range(n)]

    # Outer loop (rows): Print progress
    for i in range(n):

        # Printing calculation progress
        if prog:
            sys.stdout.write(f"\rCalculating row {i + 1}/{n}")
            sys.stdout.flush()

        # Inner loop (cols): Calculate pixel value
        for j in range(m):

            # Scaling to be between -R and R
            zx = -r + i * (2 * r / n)
            zy = -r + j * (2 * r / m)

            # Calculating next value
            iter = 0
            while zx ** 2 + zy ** 2 < r ** 2 and iter < max_iter:
                xtemp = zx ** 2 - zy ** 2
                zy = 2 * zx * zy + cy
                zx = xtemp + cx
                iter += 1
            plane[i][j] = iter

    return plane


def add_black(colormap):
    """Alters a colormap so that the highest value is black."""

    black = plt.cm.binary(255)                # doesn't conflict with vstack
    colormap = colormap(linspace(0, 1, 255))  # 255 for colormap, 1 for black
    colormap = vstack((colormap, black))      # stack both together

    # Сast to MPL colormap type
    return colors.LinearSegmentedColormap.from_list('my_colormap', colormap)


def main():
    # Input values
    n, m = list(map(int, input("Enter resolution (N, M): ").split()))
    cx, cy = list(map(float, input("Enter C constant (cx, cy): ").split()))
    max_iter = int(input("Enter max iterations per pixel (default 100): "))

    # Radius must be such that r**2 - r >= sqrt(cx**2 + cy**2)
    radius = 0
    while radius ** 2 - radius < sqrt(cx ** 2 + cy ** 2):
        radius += 0.1

    # Calculate plane
    plane = initplane(n, m, cx, cy, radius, max_iter)

    # Plot plane and save image
    cmap = add_black(plt.cm.viridis)
    norm = plt.Normalize(vmin=0, vmax=max_iter)
    image = cmap(norm(plane))
    name = f"julia_normal_{n}x{m}_c={cx}{'+' if cy > 0 else '-'}{abs(cy)}i"
    plt.imsave(f"{name}.png", image)


if __name__ == "__main__":
    main()

"""
Module to plot the Julia set (formula: `f(z) = z**2 + c`,
where `z` is a complex variable and `c` is a complex constant).
"""

import sys
import time
from math import sqrt
from random import random

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors


def initplane_np(n, c, r, max_iter, prog=True):
    """Function to calculate the plane (using numpy)."""
    # Initialize plane, iter count, function
    plane_y, plane_x = np.mgrid[r:-r:n*1j, -r:r:n*1j]
    plane = plane_x + plane_y * 1j
    iters = np.full(plane.shape, 0)
    f = lambda x: x ** 2 + c

    # Single loop (iters)
    for iter in range(max_iter):
        if prog:
            sys.stdout.write(f"\rIteration {iter + 1}/{max_iter}")
            sys.stdout.flush()
        mask = abs(plane) < r
        plane[mask] = f(plane[mask])
        iters[mask] += 1
    return iters


def initplane(n, c, r, max_iter, prog=True):
    """Function to calculate the plane (use numpy version instead)."""

    # Initializing plane
    plane = [[None] * n for _ in range(n)]

    # Outer loop (rows): Print progress
    for y in range(n):

        # Printing calculation progress
        if prog:
            sys.stdout.write(f"\rCalculating row {y + 1}/{n}")
            sys.stdout.flush()

        # Inner loop (cols): Calculate pixel value
        for x in range(n):

            # Scaling to be between -R and R
            z = (2 * r / n) * complex(x, y) - complex(r, r)

            # Calculating next value
            iter = 0
            while abs(z) < r and iter < max_iter:
                z = z ** 2 + c
                iter += 1
            plane[y][x] = iter
    return plane


def add_black(cmap):
    """Alters a colormap so that the highest value is black."""

    black = plt.cm.binary(255)           # doesn't conflict with vstack
    cmap = cmap(np.linspace(0, 1, 255))  # 255 for colormap, 1 for black
    cmap = np.vstack((cmap, black))      # stack both together

    # Сast to MPL colormap type
    return colors.LinearSegmentedColormap.from_list('my_colormap', cmap)


def main():
    # Input values
    n = int(input("Enter resolution in pixels (default 2000): "))
    max_iter = int(input("Enter max iterations per pixel (default 100): "))
    cx, cy = list(map(float, input("Enter C constant (cx, cy): ").split()))
    c = complex(cx, cy)

    # Radius must be such that r**2 - r >= sqrt(cx**2 + cy**2)
    radius = 0
    while radius ** 2 - radius < abs(c):
        radius += 0.1

    # Calculate plane
    start = time.perf_counter()
    plane = initplane_np(n, c, radius, max_iter)
    end = time.perf_counter()
    sys.stdout.write(f"\nTime to calculate plane: {end - start:.2f} seconds")

    # Plot plane and save image
    cmap = add_black(plt.cm.viridis)
    norm = plt.Normalize(vmin=0, vmax=max_iter)
    image = cmap(norm(plane))
    name = f"julia_normal_{n}px_iters={max_iter}_c={str(c).strip('()')[:-1]}i"
    plt.imsave(f"images/{name}.png", image)


if __name__ == "__main__":
    main()

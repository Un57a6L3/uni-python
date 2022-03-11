import random as r
from secrets import token_hex

from numpy import linspace
from numpy import vstack

from matplotlib import pyplot as plt
from matplotlib import colors

# THESE ARE CONFIGURABLE OPTIONS

# The matplotlib colormap to use for sprites
COLORMAP = plt.cm.viridis

# The linear size of the sprite matrix
# At least 2, recommended ~10-20
SPRITE_N = 10

# The number of images to generate
IMAGE_NUM = 4

# The range of colormap that will be present
RANGE = 0., 1.


# Adds white at the bottom of a matplotlib colormap
def add_white(colormap):
    white = plt.cm.binary(0)                  # doesn't conflict with vstack
    colormap = colormap(linspace(0, 1, 255))  # 255 because 1 is taken by white
    colormap = vstack((white, colormap))      # stack both together

    # cast to MPL colormap type
    return colors.LinearSegmentedColormap.from_list('my_colormap', colormap)


# Chooses value for each pixel
def pixel():
    if r.choice([0, 1, 2]) == 0:
        return 0
    else:
        return r.uniform(max(RANGE[0], 1/256), RANGE[1])


# Makes the matrix input to plt.imshow
def make_mx():
    mx = [[pixel() for _ in range(3)] for _ in range(5)]
    for i in mx:
        i += i[-2::-1]
    return mx


def main():
    colormap = add_white(COLORMAP)
    for _ in range(IMAGE_NUM):
        pic_name = f'gen_sprites_{COLORMAP.name}_{SPRITE_N:>02}_{token_hex(4)}'
        fig, axs = plt.subplots(SPRITE_N, SPRITE_N)
        for i in axs:
            for j in i:
                j.imshow(make_mx(), cmap=colormap)
                j.axis('off')

        plt.subplots_adjust(wspace=0.4, hspace=0.4)
        plt.savefig(pic_name, bbox_inches='tight')
        plt.close()


if __name__ == '__main__':
    main()

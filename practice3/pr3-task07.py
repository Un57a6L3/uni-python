from random import choice
from secrets import token_hex

import matplotlib.pyplot as plt


# there are 65535 possible sprites
def make_mx():
    mx = [[choice([0, 1]) for _ in range(3)] for _ in range(5)]
    for i in mx:
        i += i[-2::-1]
    return mx


def main(n):
    fig, axs = plt.subplots(n, n)
    for i in axs:
        for j in i:
            j.imshow(make_mx(), cmap='binary')
            j.axis('off')

    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.savefig(f'gen_sprites_{token_hex(5)}', bbox_inches='tight')


if __name__ == '__main__':
    main(10)

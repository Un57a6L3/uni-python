import random as r
from secrets import token_hex

import matplotlib.pyplot as plt


def make_mx():
    mx = [[r.choice([0.5, r.uniform(0, 0.45), r.uniform(0.55, 1)]) for _ in range(3)] for _ in range(5)]
    for i in mx:
        i += i[-2::-1]
    return mx


def main(n):
    fig, axs = plt.subplots(n, n)
    for i in axs:
        for j in i:
            j.imshow(make_mx(), cmap='PuOr')
            j.axis('off')

    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.savefig(f'gen_sprites_{token_hex(5)}', bbox_inches='tight')
    plt.close()


if __name__ == '__main__':
    for _ in range(25):
        main(5)

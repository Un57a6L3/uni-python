import matplotlib.pyplot as plt
import matplotlib as mpl

seed = [0x5A4A, 0x0248, 0xB753]
pairs = '..LEXEGEZACEBISO' \
        'USESARMAINDIREA.' \
        'ERATENBERALAVETI' \
        'EDORQUANTEISRION'

x = list()
y = list()
n = list()


def tweakseed():
    temp = sum(seed) % 0x10000  # imitate uint16 overflow
    seed[0] = seed[1]
    seed[1] = seed[2]
    seed[2] = temp


def makesystem():
    longnameflag = seed[0] & 64
    name = list()
    x_coord = seed[1] >> 8
    y_coord = 255 - seed[0] >> 8

    pair1 = 2 * ((seed[2] >> 8) & 31)
    tweakseed()
    pair2 = 2 * ((seed[2] >> 8) & 31)
    tweakseed()
    pair3 = 2 * ((seed[2] >> 8) & 31)
    tweakseed()
    pair4 = 2 * ((seed[2] >> 8) & 31)
    tweakseed()

    name.append(pairs[pair1])
    name.append(pairs[pair1 + 1])
    name.append(pairs[pair2])
    name.append(pairs[pair2 + 1])
    name.append(pairs[pair3])
    name.append(pairs[pair3 + 1])

    if longnameflag:
        name.append(pairs[pair4])
        name.append(pairs[pair4 + 1])

    name = ''.join([ch for ch in name if ch != '.'])
    return x_coord, y_coord, name


def main():
    mpl.style.use('dark_background')
    plt.figure(figsize=(24, 12))
    for i in range(256):
        tx, ty, tn = makesystem()
        x.append(tx)
        y.append(ty)
        n.append(tn)

    plt.scatter(x, y, s=2, color='white')
    for i, txt in enumerate(n):
        plt.annotate(txt, (x[i] + 0.5, y[i] + 0.5))

    plt.axis('off')
    plt.savefig('gen_galaxy', bbox_inches='tight')


if __name__ == '__main__':
    main()

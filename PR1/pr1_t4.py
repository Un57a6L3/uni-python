def mp12(x):
    x = x + x + x
    x = x + x
    x = x + x
    return x


def mp16(x):
    x = x + x
    x = x + x
    x = x + x
    x = x + x
    return x


def mp15(x):
    y = x
    x = x + x
    x = x + x
    x = x + x
    x = x - (y - x)
    return x


def mp29(x):
    y = x
    x = x + x
    y = y + x
    x = x + x
    x = x + x
    x = x + x
    x = x + x
    x = x - y
    return x


def main():
    x = int(input("Enter x: "))
    print(mp12(x))
    print(mp16(x))
    print(mp15(x))
    print(mp29(x))


if __name__ == '__main__':
    main()

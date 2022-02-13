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
    x = int(input("Enter number to multiply: "))
    print(f"{x} times 12 equals {mp12(x)}")
    print(f"{x} times 16 equals {mp16(x)}")
    print(f"{x} times 15 equals {mp15(x)}")
    print(f"{x} times 29 equals {mp29(x)}")


if __name__ == '__main__':
    main()

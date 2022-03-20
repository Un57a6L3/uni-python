from math import sin


def main(x):
    if x < -3:
        return 46 * x ** 4 + 1
    elif x < 12:
        return 72 * x - (14 * x - 7)
    elif x < 36:
        return (x ** 3 - 82 * x - x ** 2) ** 6 +\
               81 * x + 77 * (87 * x ** 2) ** 7
    else:
        return (66 * x + x ** 3) ** 5 + 8 * sin(x) ** 4


# cut this out when submitting to robot
if __name__ == "__main__":
    f = main(float(input("Enter x: ")))
    print(f"{f:.2e}")

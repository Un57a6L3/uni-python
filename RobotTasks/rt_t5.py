from math import ceil


def main(z):
    n = len(z)
    sum_i = 0
    for i in range(1, n+1):
        sum_i += z[n - ceil(i / 2)] ** 4 / 67
    return sum_i


# cut this out when submitting to robot
if __name__ == "__main__":
    n = int(input("Enter vector length: "))
    z = list(map(float, input("Enter vector: ").split()))
    f = main(z)
    print(f"{f:.2e}")

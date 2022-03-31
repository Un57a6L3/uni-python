def f(n):
    if not n:
        return 0.28
    elif n >= 1:
        prev = f(n - 1)
        return prev ** 2 / 32 + 0.04 + prev


def main(n):
    return f(n)


# cut this out when submitting to robot
if __name__ == "__main__":
    f = main(int(input("Enter n: ")))
    print(f"{f:.2e}")

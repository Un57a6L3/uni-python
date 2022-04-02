from math import floor


def par1(c):
    return 82 * c - floor(c) ** 4 - (31 * c + 47 * c ** 2 + c ** 3) ** 5


def par2(j, c, k, p):
    return 79 * j ** 3 + 50 * k ** 5 + (c / 90 - 1 - p ** 3) ** 7


def main(b, m, n, p):
    sum_c = 0
    for c in range(1, b + 1):
        sum_c += par1(c)

    sum_j = 0
    for j in range(1, n + 1):
        prod_c = 1
        for c in range(1, b + 1):
            sum_k = 0
            for k in range(1, m + 1):
                sum_k += par2(j, c, k, p)
            prod_c *= sum_k
        sum_j += prod_c

    return sum_c + sum_j


# --- cut this out when submitting to robot ---
B, M, N = list(map(int, input("Enter b, m, n: ").split()))
P = float(input("Enter p: "))
print(f"{main(B, M, N, P):.2e}")

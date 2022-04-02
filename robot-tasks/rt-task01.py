from math import floor


def main(z):
    return (z ** 2 / 45) - (70 * (z ** 2 - 62 * z ** 3 - 58) ** 3) +\
           ((41 * floor(z) - 53 * (74 * z ** 2 - z) ** 7) / z ** 5)


# --- cut this out when submitting to robot ---
f = main(float(input("Enter z: ")))
print(f"{f:.2e}")

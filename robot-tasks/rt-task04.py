def main(n):
    if not n:
        return 0.28
    elif n >= 1:
        prev = main(n - 1)
        return prev ** 2 / 32 + 0.04 + prev


# --- cut this out when submitting to robot ---
f = main(int(input("Enter n: ")))
print(f"{f:.2e}")

# Simplified version of fast_mul_gen function
# Prints only the function's body
def fast_mul_gen_body(y):
    print("res = 0")
    while y > 1:
        if y % 2:
            print("res = res + x")
        print("x = x + x")
        y //= 2
    print("res = res + x")
    print("return res")


# Prints full function definition and its call
# Default generation function
def fast_mul_gen(y):
    func = f"mul_{y}"
    print(f"def {func}(x):")
    print("\tres = 0")
    while y > 1:
        if y % 2:
            print("\tres = res + x")
        print("\tx = x + x")
        y //= 2
    print("\tres = res + x")
    print("\treturn res")
    print(f"\n\nx = int(input(\"Enter x: \"))")
    print(f"print({func}(x))")


# An improvement of the fast_mul_gen function
# Generates a function with subtraction if that is shorter
# Otherwise behaves the same as fast_mul_gen
def fast_mul_gen_subtr(y):
    # counting zeroes and length
    mask = 1
    length = 0
    zerocount = 0
    while mask < y:
        if not mask & y:
            zerocount += 1
        length += 1
        mask <<= 1

    # function header
    func = f"mul_{y}"
    print(f"def {func}(x):")

    # function with subtraction
    if zerocount < length / 2:
        print("\tres = 0 - x")
        while y > 1:
            if not y % 2:
                print("\tres = res - x")
            print("\tx = x + x")
            y //= 2
        print("\tx = x + x")

    # function with no subtraction (same as fast_mul_gen)
    else:
        print("\tres = 0")
        while y > 1:
            if y % 2:
                print("\tres = res + x")
            print("\tx = x + x")
            y //= 2

    # function finish and call
    print("\tres = res + x")
    print("\treturn res")
    print(f"\n\nx = int(input(\"Enter x: \"))")
    print(f"print({func}(x))")


def main():
    x = int(input("Enter factor for function generation: "))
    print("----- ----- Output ----- -----")
    print()
    # fast_mul_gen_body(x)
    # fast_mul_gen(x)
    fast_mul_gen_subtr(x)


if __name__ == '__main__':
    main()

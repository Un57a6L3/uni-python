# Prints only the body of function
def fast_mul_gen(y):
    print("res = 0")
    while y > 1:
        if y % 2:
            print("res = res + x")
        print("x = x + x")
        y //= 2
    print("res = res + x")
    print("return res")


# Prints full function definition and its call
def fast_mul_gen_full(y):
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


def main():
    x = int(input("Enter x: "))
    fast_mul_gen_full(x)


if __name__ == '__main__':
    main()

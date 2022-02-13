def fast_mul(a, b):
    res = 0
    while a > 1:
        if a % 2:
            res += b
        a //= 2
        b *= 2
    if a != 0:
        res += b
    return res


def fast_pow(number, power):
    res = number
    for i in range(power - 1):
        res = fast_mul(number, res)
    return res


# This function was for debugging why the code gave wrong answers
# The exact same code had worked perfectly on a uni computer
# Turns out it had Python 2, where operator / returns integer value
# Online terminals and my machine has Python 3, where / returns float
# After replacing operator / with operator // the code works fine
# So this function is (hopefully) not needed anymore
def fast_mul_debug(a, b):
    print(f"Running fast_mul({a}, {b})")
    res = 0
    count = 0
    print(f"res set to {res}")
    while a > 1:
        count += 1
        print(f"While-loop iteration {count}:")
        if a % 2:
            print(f"If-statement passed: {a} % 2 == {a % 2}")
            res += b
            print(f"res now equals {res} after adding {b}")
        else:
            print(f"If-statement failed: {a} % 2 == {a % 2}")
        a /= 2
        b *= 2
        print(f"a divided by 2 and equals {a}")
        print(f"b multiplied by 2 and equals {b}")
    res += b
    print(f"Out of loop after {count} iterations")
    print(f"a = {a}, b = {b}, res now equals {res} which is returned")
    return res


def test_fast_mul():
    from random import randrange
    passed = True
    fails = set()
    for i in range(0, 10):
        a = randrange(100)
        b = randrange(100)
        print(f'Test {i} for numbers {a}, {b}')
        if fast_mul(a, b) == a * b:
            print(f'Test passed | Result: {fast_mul(a, b)}')
        else:
            print(f'Test failed | Result: {fast_mul(a, b)} | Expected result: {a * b}')
            passed = False
            fails.add(i)
    if passed:
        print('Testing passed')
    else:
        print(f'Testing failed | Failed tests: {fails}')


def main():
    a = int(input("Enter first factor: "))
    b = int(input("Enter second factor: "))
    print(f"{a} times {b} equals {fast_mul(a, b)}")
    print()

    a = int(input("Enter base number: "))
    b = int(input("Enter exponent (power): "))
    print(f"{a} to the power of {b} equals {fast_pow(a, b)}")
    print()

    input("Enter anything to test fast_mul: ")
    print("--- Automatic testing of fast_mul function ---")
    test_fast_mul()


if __name__ == '__main__':
    main()

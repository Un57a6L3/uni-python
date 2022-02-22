# 1: Cast elements in s from string to integer
def subtask1(s):
    return list(map(int, s))


# 2: Count unique elements in s
def subtask2(s):
    return len(set(s))


# 3: Reverse s without functions
def subtask3(s):
    return s[::-1]


# 4: Make list of indexes of occurrences of x in list s
def subtask4(s, x):
    return [i for i in range(len(s)) if s[i] == x]


# 5: Sum elements in s with even indexes
def subtask5(s):
    return sum(s[::2])


# 6: Find the longest string in s
# Oh god this is utterly ridiculous
# Who the hell endorses such codestyle?
def subtask6(s):
    return s[[len(s[i]) for i in range(len(s))].index((max([len(s[i]) for i in range(len(s))])))]


def main():
    s = list(input("Enter number list: ").split())
    print(f'Before cast: {s}')
    s = subtask1(s)
    print(f'After cast: {s}')
    print(f'List s has {subtask2(s)} unique elements')
    print(f'Reversed list s: {subtask3(s)}')
    x = int(input('Enter number to find in list s: '))
    print(f'{x} occurs in list s at indexes {subtask4(s, x)}')
    print(f'The sum of elements in list s at even indexes equals {subtask5(s)}')
    s = list(input("Enter string list: ").split())
    print(f'List s now is: {s}')
    print(f'The longest string in list s is {subtask6(s)}')


if __name__ == '__main__':
    main()

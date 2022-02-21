def oneliners():
    s = list()
    s.append("65")
    s.append("76")
    s.append("354")
    s.append("76")

    # task1 - cast elements in s from string to integer
    s = list(map(int, s))
    print(s)

    # task2 - count unique elements in s
    result = len(set(s))
    print(result)

    # task3 - reverse s without functions
    result = s[::-1]
    print(result)

    # task4 - make list of indexes of occurrences of x in list s
    x = 76  # key
    result = [i for i in range(len(s)) if s[i] == x]
    print(result)

    # task5 - sum elements in s with even indexes
    result = sum(s[::2])
    print(result)

    s = ["sample", "text", "lol", "lorem", "ipsum"]

    # task6 - find the longest string in s
    # might not be the most optimal solution, but I'm yet to find one
    result = s[[len(s[i]) for i in range(len(s))].index((max([len(s[i]) for i in range(len(s))])))]
    print(result)


# idk how to solve this yet
def str_select():
    i = 0

    # original
    result = ['much','code','wow'][i]
    print(result)

    # my solution ??????
    i *= 4
    result = 'muchcodewow'[i]
    print(result)
    # 0 - 0:4
    # 1 - 4:8
    # 2 - 8:11


def main():
    oneliners()


if __name__ == '__main__':
    main()

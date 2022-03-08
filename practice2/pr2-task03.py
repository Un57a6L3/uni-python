# Function that generates the student groups list
# They must be identical to list on kispython.ru
def generate_groups():
    # setting data list
    year = 20
    codes = [
        ["ИВБО", list(range(1, 9)) + [13]],
        ["ИКБО", list(range(1, 28)) + [30]],
        ["ИНБО", list(range(1, 12)) + [13, 15]],
        ["ИМБО", [1, 2]]
    ]

    # generating string list
    groups = list()
    for x in codes:
        groups.append([f'{x[0]}-{i:02d}-{year}' for i in x[1]])

    # printing generated list
    for x in groups:
        print(x)


def main():
    generate_groups()


if __name__ == '__main__':
    main()

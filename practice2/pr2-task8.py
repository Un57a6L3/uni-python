from random import randrange


# Function for generating random full names
def generate_fullname():
    # first names samples pool
    firstnames_start = ["Ант", "Арс", "Арт", "Ал", "Бор", "Викт", "Гор", "Дмит", "Ел", "Ем", "Жор", "Зах"]
    firstnames_end = ["он", "ен", "ем", "екс", "ис", "ат", "ор", "рий", "ей", "еля", "ар"]

    # middle names letters pool
    middlenames = [f'{chr(i)}.' for i in range(ord('А'), ord('Я') + 1)]
    middlenames.remove('Ъ.')
    middlenames.remove('Ы.')
    middlenames.remove('Ь.')

    # last names endings pool
    lastnames_end = ["ов", "ин", "ский", "як", "ко", "цкий", "ич", "ишвили", "ян", "ан", "евич", "ович", "юк"]

    # first name generation
    fullname = firstnames_start[randrange(len(firstnames_start))] + firstnames_end[randrange(len(firstnames_end))]
    if not randrange(3):
        fullname += firstnames_end[randrange(len(firstnames_end))]

    # middle name selection
    fullname += " " + middlenames[randrange(len(middlenames))] + " "

    # last name generation
    fullname += firstnames_start[randrange(len(firstnames_start))]
    if randrange(2):
        fullname += firstnames_end[randrange(len(firstnames_end))]
    fullname += lastnames_end[randrange(len(lastnames_end))]
    return fullname


def main():
    for i in range(10):
        print(generate_fullname())


if __name__ == '__main__':
    main()

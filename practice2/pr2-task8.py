from random import randrange


def generate_fullname():
    firstnames_start = ["Ант", "Арс", "Арт", "Ал", "Бор", "Викт", "Гор", "Дмит", "Ел", "Ем", "Жор", "Зах"]
    firstnames_end = ["он", "ен", "ем", "екс", "ис", "ат", "ор", "рий", "ей", "еля", "ар"]

    middlenames = [f'{chr(i)}.' for i in range(ord('А'), ord('Я') + 1)]
    middlenames.remove('Ъ.')
    middlenames.remove('Ы.')
    middlenames.remove('Ь.')

    lastnames_end = ["ов", "ин", "ский", "як", "ко", "цкий", "ич", "ишвили", "ян", "ан", "евич", "ович", "юк"]

    fullname = firstnames_start[randrange(len(firstnames_start))] + firstnames_end[randrange(len(firstnames_end))]
    if not randrange(3):
        fullname += firstnames_end[randrange(len(firstnames_end))]
    fullname += " " + middlenames[randrange(len(middlenames))] + " "
    fullname += firstnames_start[randrange(len(firstnames_start))]
    if randrange(2):
        fullname += firstnames_end[randrange(len(firstnames_end))]
    fullname += lastnames_end[randrange(len(lastnames_end))]
    return fullname


def main():
    print(generate_fullname())


if __name__ == '__main__':
    main()

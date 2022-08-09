import re


# Function for parsing group name and variant from input string
def parse_subj(text):
    text = str.lower(text)

    # detecting group name substring
    str_gr = '\n'
    str_gr_src = ['ivbo', 'ивбо', 'ikbo', 'икбо', 'inbo', 'инбо', 'imbo', 'имбо']
    for substr in str_gr_src:
        if substr in text:
            str_gr = substr
            break

    # formatting string to remove group name
    ind_gr = text.find(str_gr)
    text.replace(str_gr, '#' * len(str_gr))

    # detecting variant substring
    str_var = '\n'
    str_var_src = ['variant', 'вариант', 'var', 'вар', 'v.', 'v:', 'v-', 'в.', 'в:', 'в-', 'v', 'в']
    for substr in str_var_src:
        if substr in text:
            str_var = substr
            break

    # formatting string to remove variant
    ind_var = text.find(str_var)
    text.replace(str_var, '#' * len(str_var))

    # getting a list of all integers in string
    nums = re.findall(r'\d+', text)

    years = ['18', '19', '20']
    number = ''
    variant = ''

    # assigning integers depending on substring order
    if ind_gr < ind_var or ind_var == -1:
        if len(nums) == 2:
            number, variant = nums[0][:2], nums[1]
        elif len(nums) == 3 and nums[1] in years:
            number, variant = nums[0], nums[2]
    elif ind_gr > ind_var:
        if len(nums) == 2:
            number, variant = nums[1][:2], nums[0]
        elif len(nums) == 3 and nums[2] in years:
            number, variant = nums[1], nums[0]

    # transforming group name string to capital russian
    group = {
        'ivbo': 'ИВБО', 'ивбо': 'ИВБО',
        'ikbo': 'ИКБО', 'икбо': 'ИКБО',
        'inbo': 'ИНБО', 'инбо': 'ИНБО',
        'imbo': 'ИМБО', 'имбо': 'ИМБО'
    }.get(str_gr, '')
    return group, number, variant


def main():
    text = input('Enter letter header: ')
    result = parse_subj(text)

    if result[0] != '':
        print('Направление: ' + result[0])
    else:
        print('Не удалось определить направление')
    if result[1] != '':
        print('Номер группы: ' + result[1])
    else:
        print('Не удалось определить номер группы')
    if result[2] != '':
        print('Вариант: ' + result[2])
    else:
        print('Не удалось определить вариант')


if __name__ == '__main__':
    main()

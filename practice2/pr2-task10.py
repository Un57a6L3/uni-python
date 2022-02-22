import re


# Function for parsing group name and variant from input string
def parse_subj(text):
    text = str.lower(text)

    # detecting group name substring
    str_gr = ''
    if 'ivbo' in text:
        str_gr = 'ivbo'
    elif 'ивбо' in text:
        str_gr = 'ивбо'
    elif 'ikbo' in text:
        str_gr = 'ikbo'
    elif 'икбо' in text:
        str_gr = 'икбо'
    elif 'inbo' in text:
        str_gr = 'inbo'
    elif 'инбо' in text:
        str_gr = 'инбо'
    elif 'imbo' in text:
        str_gr = 'imbo'
    elif 'имбо' in text:
        str_gr = 'имбо'

    # formatting string to remove group name
    ind_gr = text.find(str_gr)
    text.replace(str_gr, '#' * len(str_gr))

    # detecting variant substring
    str_var = ''
    if 'variant' in text:
        str_var = 'variant'
    elif 'вариант' in text:
        str_var = 'вариант'
    elif 'var' in text:
        str_var = 'var'
    elif 'вар' in text:
        str_var = 'вар'
    elif 'v.' in text:
        str_var = 'v.'
    elif 'v:' in text:
        str_var = 'v:'
    elif 'v-' in text:
        str_var = 'v-'
    elif 'в.' in text:
        str_var = 'в.'
    elif 'в:' in text:
        str_var = 'в:'
    elif 'в-' in text:
        str_var = 'в-'
    elif 'v' in text:
        str_var = 'v'
    elif 'в' in text:
        str_var = 'в'

    # formatting string to remove variant
    ind_var = text.find(str_var)
    text.replace(str_var, '#' * len(str_var))

    # getting a list of all integers in string
    nums = re.findall(r'\d+', text)

    years = ['18', '19', '20']
    number = ''
    variant = ''

    # assigning integers depending on substring order
    if ind_gr < ind_var:
        if len(nums) == 2:
            number = nums[0]
            variant = nums[1]
        elif len(nums) == 3 and nums[1] in years:
            number = nums[0]
            variant = nums[2]
    elif ind_gr > ind_var:
        if len(nums) == 2:
            number = nums[1]
            variant = nums[0]
        elif len(nums) == 3 and nums[2] in years:
            number = nums[1]
            variant = nums[0]

    # transforming group name string to capital russian
    group = ''
    if str_gr == 'ivbo' or str_gr == 'ивбо':
        group = 'ИВБО'
    elif str_gr == 'ikbo' or str_gr == 'икбо':
        group = 'ИКБО'
    elif str_gr == 'inbo' or str_gr == 'инбо':
        group = 'ИНБО'
    elif str_gr == 'imbo' or str_gr == 'имбо':
        group = 'ИМБО'

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

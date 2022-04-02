def main(table):
    parsed = set()
    percent, state, datedot = [], [], []
    for num, flag, _, date in table:
        if num in parsed or num is None:
            continue
        parsed.add(num)
        percent.append((f'{float(num):.0%}'))
        state.append('Выполнено' if int(flag) else 'Не выполнено')
        datedot.append(f'{date[-2:]}.{date[3:5]}.{date[:2]}')
    return [percent, state, datedot]


# --- cut this out when submitting to robot ---
t = [
    [None, None, None, None],
    [None, None, None, None],
    ['0.3493', '0', '0.3493', '12-08-2001'],
    ['0.6497', '0', '0.6497', '28-09-2000'],
    ['0.3493', '0', '0.3493', '12-08-2001'],
    ['0.8170', '0', '0.8170', '26-03-2000'],
    ['0.3493', '0', '0.3493', '12-08-2001']
]
res = main(t)
print(res)

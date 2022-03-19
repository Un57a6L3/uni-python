import sys
from datetime import datetime
from traceback import format_tb


# Function that throws exceptions
def error_maker(num):
    match num:
        case 0:  # ZeroDivisionError
            return 1 / 0
        case 1:  # IndexError
            return [0, 1, 2][3]
        case 2:  # ValueError
            return int('xyz')
        case 3:  # KeyError
            return {0: 0, 1: 1}[2]
        case _:  # TypeError
            return '2' + 2


# Function for logging exceptions
def run_with_log(func, *args):
    def my_excepthook(exctype, value, traceback):
        date = f"{datetime.now():%H:%M:%S %d-%m-%Y}"
        tb = 'Traceback (most recent call last):\n' + \
             ''.join(format_tb(traceback))
        with open('foo.log', 'a') as log:
            log.write(f"{date}\n{tb}{exctype.__name__}: {value}\n\n")

    sys.excepthook = my_excepthook
    func(*args)


if __name__ == '__main__':
    x = int(input("Select from 0 to 4: "))
    run_with_log(error_maker, x)

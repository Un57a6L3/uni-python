import logging


def foo():
    a = 1 / 0
    return a


def run_with_log(func):
    logging.basicConfig(filename='foo.log', level=logging.DEBUG)
    try:
        func()
    except:
        logging.exception('log')


if __name__ == '__main__':
    run_with_log(foo)

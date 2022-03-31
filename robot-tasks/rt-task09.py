class main:
    def __init__(self):
        self.__state = 'A'

    def sweep(self):
        if self.__state == 'A':
            self.__state = 'B'
            return 0
        if self.__state == 'B':
            self.__state = 'C'
            return 2
        if self.__state == 'E':
            self.__state = 'F'
            return 7
        raise KeyError

    def drag(self):
        if self.__state == 'B':
            return 3
        if self.__state == 'F':
            return 8
        raise KeyError

    def make(self):
        if self.__state == 'A':
            self.__state = 'E'
            return 1
        if self.__state == 'B':
            self.__state = 'F'
            return 4
        if self.__state == 'C':
            self.__state = 'D'
            return 5
        if self.__state == 'D':
            self.__state = 'E'
            return 6
        raise KeyError


# cut this out when submitting to robot
if __name__ == '__main__':
    o = main()
    print(o.sweep())
    print(o.drag())
    print(o.drag())
    print(o.drag())
    print(o.sweep())
    print(o.drag())
    print(o.make())
    print(o.make())
    print(o.sweep())
    print(o.sweep())
    print(o.drag())
    print(o.drag())

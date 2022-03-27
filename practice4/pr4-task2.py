
class TestClass():
    '''Class for sample object'''

    def __init__(self):
        self.a = 'muchcodewow'
        self.b = 42
        self.c = None

    def test(self):
        print("Test call")


def main():
    a = TestClass()
    print(vars(a))
    getattr(a, 'test')()


if __name__ == "__main__":
    main()

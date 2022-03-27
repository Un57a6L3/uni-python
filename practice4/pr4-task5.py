class HTML:
    '''Main class that keeps the code string'''

    def __init__(self):
        self.code = []

    def get_code(self):
        return '\n'.join(self.code)

    def body(self):
        return HTML_Body(self)

    def div(self):
        return HTML_Div(self)

    def p(self, msg):
        self.code.append(f'<p>{msg}</p>')


class HTML_Body:
    '''Context manager class for <body> element'''

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        self.obj.code.append('<body>')

    def __exit__(self, *exc):
        self.obj.code.append('</body>')


class HTML_Div:
    '''Context manager class for <div> element'''

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        self.obj.code.append('<div>')

    def __exit__(self, *exc):
        self.obj.code.append('</div>')


def main():
    html = HTML()
    with html.body():
        pass
        with html.div():
            with html.div():
                html.p('Python PR4 Task 5')
                html.p('Code by Arseny Antonov')
            with html.div():
                html.p('Group IKBO-02-20')
    print(html.get_code())


if __name__ == '__main__':
    main()

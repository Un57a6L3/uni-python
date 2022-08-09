from collections import namedtuple
from random import choice


def formstring(hor, iver, over, substrs, sides, center):
    """
    Adds borders and delimiters to a table line.
    Used within the `tabulate` function.

    Horizontal delimiter should be `space` if the line has table items.

    :param hor: Horizontal delimiter
    :param iver: Inner vertical delimiter
    :param over: Outer vertical delimiter
    :param substrs: List of table cells to format
    :param sides: Whether there is an outer vertical border
    :param center: Whether there is an inner vertical border
    :returns: Formatted string ready to print
    """

    # Form inner and outer dividers
    innerDivider = iver.join([hor] * 2) if center else ' '
    outerDivider = f"{over}{hor}" if sides else ''

    # Form the final divider string
    line = innerDivider.join(substrs)
    line = f"{outerDivider}{line}{outerDivider[::-1]}"
    return line


def tabulate(table, headers=None, tablefmt="simple"):
    """
    Fancy table formatting with ascii pseudo-graphics.
    Based on `tabulate` module at https://github.com/astanin/python-tabulate.

    :param table: Tabular data to format (e.g. list of lists)
    :param headers: List of table headers, `None` by default
    :param tablefmt: Table formatting style, `"simple"` by default

    Example formatting:
    ```repl
    >>> table = [['foo', 456], ['baaaar', 6724], ['tar.gz', 32]]
    >>> headers = ['name', 'num']
    >>> print(tabulate(table, headers, tablefmt="github")) 
    | name   | num  |
    |--------|------|
    | foo    |  456 |
    | baaaar | 6724 |
    | tar.gz |   32 |
    ```
    """

    # All the table formatting styles are defined with these delimiters
    Div = namedtuple('Div', [
        'afterHeader',
        'innerVertical',
        'innerHorizontal',
        'innerIntersection',
        'outerVertical',
        'outerHorizontal',
        'outerIntersection'
    ])

    # Collection of table formatting styles, in alphabetical order
    styles = {  # ......AH....IV....IH....II....OV....OH....OI....
        "github":   Div('-',  '|',  None, '|',  '|',  None, '|'),
        "grid":     Div('=',  '|',  '-',  '+',  '|',  '-',  '+'),
        "orgtbl":   Div('-',  '|',  None, '+',  '|',  None, '|'),
        "outline":  Div('=',  '|',  None, '+',  '|',  '-',  '+'),
        "plain":    Div(None, None, None, None, None, None, None),
        "presto":   Div('-',  '|',  None, '+',  None, None, None),
        "pretty":   Div('-',  '|',  None, '+',  '|',  '-',  '+'),
        "rst":      Div('=',  None, None, None, None, '=',  None),
        "simple":   Div('-',  None, None, None, None, None, None),
        "test":     Div('~',  '|',  '-',  '+',  '‖',  '=',  '#'),
    }

    # Select table formatting style
    if tablefmt == "random":
        tablefmt = choice(list(styles.keys()))
    div = styles.get(tablefmt, None)
    if div is None:
        raise NameError

    # Get table dimensions
    rows = len(table)
    cols = max([len(x) for x in table]) if headers is None else len(headers)

    # Get maximum row length for each column
    maxstrlen = [0] * cols
    for col in range(cols):
        if headers is not None:
            maxstrlen[col] = len(str(headers[col]))
        for row in table:
            maxstrlen[col] = max(len(str(row[col])), maxstrlen[col])

    # Set flags for outer and inner vertical borders
    outerVB = False if div.outerVertical is None else True
    innerVB = False if div.innerVertical is None else True

    # Form all horizontal border lines
    lines = []
    for hor in [div.afterHeader, div.innerHorizontal, div.outerHorizontal]:
        if hor is None:
            lines.append(None)
            continue
        substrs = [f"{hor * x}" for x in maxstrlen]
        line = formstring(hor, div.innerIntersection,
                          div.outerIntersection, substrs, outerVB, innerVB)
        lines.append(line)
    afterHeaderLine, innerHorizontalLine, outerHorizontalLine = lines

    printList = list()

    # Begin with outer horizontal line
    printList.append(outerHorizontalLine)

    # Print header line and after header line
    if headers is not None:

        # Set spacing for items
        headerLine = list()
        for col in range(cols):
            text = headers[col]
            spaces = ' ' * (maxstrlen[col] - len(str(text)))
            headerLine.append(f"{text}{spaces}")

        # Join and print items
        headerLine = formstring(' ', div.innerVertical,
                                div.outerVertical, headerLine, outerVB, innerVB)
        printList.append(headerLine)
        printList.append(afterHeaderLine)

    # Print table rows and divider lines
    for row in range(rows):

        # Print divider line
        if row != 0:
            printList.append(innerHorizontalLine)

        # Set spacing for items
        itemLine = list()
        for col in range(cols):
            text = table[row][col]
            spaces = ' ' * (maxstrlen[col] - len(str(text)))
            itemLine.append(f"{text}{spaces}")

        # Join and print items
        itemLine = formstring(' ', div.innerVertical,
                              div.outerVertical, itemLine, outerVB, innerVB)
        printList.append(itemLine)

    # Finish with outer horizontal line
    printList.append(outerHorizontalLine)
    return '\n'.join([x for x in printList if x is not None])


# Usage example, not executed on import
if __name__ == "__main__":
    table = [['foo', 456], ['baaaar', 6724], ['tar.gz', 32]]
    headers = ['name', 'num']
    print(tabulate(table, headers=headers, tablefmt="random"))

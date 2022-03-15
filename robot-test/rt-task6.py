def main(x):
    if x[0] == 'ORG':
        if x[1] == 1967:
            if x[4] == 'CHUCK':
                if x[2] == 2015:
                    return 0
                elif x[2] == 2019:
                    return 1
                elif x[2] == 2008:
                    return 2
            elif x[4] == 'CUDA':
                return 3
            elif x[4] == 'RDOC':
                if x[3] == 'XSLT':
                    return 4
                elif x[3] == 'RED':
                    return 5
        elif x[1] == 1996:
            if x[4] == 'CHUCK':
                if x[3] == 'XSLT':
                    return 6
                elif x[3] == 'RED':
                    return 7
            elif x[4] == 'CUDA':
                if x[2] == 2015:
                    return 8
                elif x[2] == 2019:
                    return 9
                elif x[2] == 2008:
                    return 10
            elif x[4] == 'RDOC':
                return 11
    elif x[0] == 'PHP':
        return 12
    return -1


if __name__ == '__main__':
    x = ['PHP', 1996, 2019, 'RED', 'CHUCK']
    y = ['ORG', 1967, 2008, 'XSLT', 'CHUCK']
    print(main(x))
    print(main(y))

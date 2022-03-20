def choicex2(cond, x):
    if cond == 2015:
        return x
    elif cond == 2019:
        return x + 1
    return x + 2


def choicex3(cond, x):
    if cond == 'XSLT':
        return x
    return x + 1


def main(x):
    if x[0] == 'ORG':
        if x[1] == 1967:
            if x[4] == 'CHUCK':
                return choicex2(x[2], 0)
            elif x[4] == 'CUDA':
                return 3
            return choicex3(x[3], 4)
        elif x[1] == 1996:
            if x[4] == 'CHUCK':
                return choicex3(x[3], 6)
            elif x[4] == 'CUDA':
                return choicex2(x[2], 8)
            return 11
    return 12


# cut this out when submitting to robot
if __name__ == '__main__':
    X = ['PHP', 1996, 2019, 'RED', 'CHUCK']
    Y = ['ORG', 1967, 2008, 'XSLT', 'CHUCK']
    print(main(X))
    print(main(Y))

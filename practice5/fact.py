def fact(n: int) -> int:
    '''Factorial function implementation.'''
    result = 1
    positive = True
    if n < 0:
        n *= -1
        if n % 2:
            positive = False
    while(n > 0):
        result *= n
        n -= 1
    if not positive:
        result *= -1
    return result

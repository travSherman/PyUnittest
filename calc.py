def triple(x):
    """triples number"""

    if not (isinstance(x, int)):
        raise ValueError('Input an integer')

    return x * 3

def cubed(x):
    """Cubes nuber"""

    if not (isinstance(x, int)):
        raise ValueError('Input an integer')
    return x ** 3

def addThenCubed(x, y):
    """Adds both number and cubes the sum"""

    if not (isinstance(x, int)):
        raise ValueError('Input an integer')

    if not (isinstance(y, int)):
        raise ValueError('Input an integer')

    return (x + y) ** 3

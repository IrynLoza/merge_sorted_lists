"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """
    c = [0] * (len(a) + len(b))
        
    i=y=j=0
    while i < len(a) and y < len(b):
        if a[i] <= b[y]:
            c[j] = a[i]
            i+= 1
            j+= 1
        else:
            c[j] = b[y]
            y+= 1
            j+= 1
    #one of l is empty
    while i < len(a):
        c[j] = a[i]
        i+= 1
        j+= 1
    while y < len(b):
        c[j] = b[y]
        y+= 1
        j+= 1
    return c    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n")

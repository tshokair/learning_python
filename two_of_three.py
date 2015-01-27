def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    "*** YOUR CODE HERE ***"
    if a >=b and a>=c:
        if b>=c:
            return a*a+b*b
        else:
            return a*a+c*c
    elif b>=a and b>=c:
        if a>c:
            return a*a+b*b
        else:
            return b*b+c*c
    elif c>=a and c>=b:
        if a>=b:
            return a*a+c*c
        else:
            return b*b+c*c

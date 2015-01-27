#!/usr/bin/env python
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
        length.
        
        >>> a = hailstone(10)
        10
        5
        16
        8
        4
        2
        1
        >>> a
        7
        """
    print(n)
    new_n = n
    while new_n!=1:
        if(new_n%2==0):
            new_n =int(new_n/2)
        else:
         new_n =int(new_n*3+1)
    return new_n
a=hailstone(10)
a

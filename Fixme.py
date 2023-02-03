#!/usr/bin/python3

def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''

    ns = range(n + 1)
    result = filter(lambda n: n % 2 == 0, ns)
    return list(result)

#!/usr/bin/python3

'''
Complete each function below so that the test cases pass.
Your solutions should use the map and filter functions,
and not for loops or list comprehensions.
'''


def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.


    >>> evens(10)
    [0, 2, 4, 6, 8, 10]
    >>> evens(11)
    [0, 2, 4, 6, 8, 10]
    >>> evens(0)
    [0]
    >>> evens(1)
    [0]
    >>> evens(-1)
    []
    '''
    evenslist = range(n+1)
    evenslist = filter(lambda x: x % 2 == 0, evenslist)
    return list(evenslist)


def threes(n):
    '''
    Returns a list of all number from 0 to n inclusive that contain the digit 3

    >>> threes(2)
    []
    >>> threes(3)
    [3]
    >>> threes(10)
    [3]
    >>> threes(20)
    [3, 13]
    >>> threes(50)
    [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43]
    '''
    threeslist = range(n+1)
    threeslist = filter(lambda x: '3' in str(x), threeslist)
    y = list(threeslist)
    return y


def small_words(text):
    '''

    HINT:
    Recall that text.split() converts the text variable into a list of words.

    >>> small_words('this is a simple test case')
    ['this', 'is', 'a', 'test', 'case']
    >>> small_words('really enormous words')
    []
    >>> small_words('')
    []
    >>> small_words('a big word is bad')
    ['a', 'big', 'word', 'is', 'bad']
    '''
    words = text.split()
    smallwordslist = filter(lambda x: len(x) < 5, words)
    return list(smallwordslist)


def squares(n):
    '''
    Returns a list of all square number between 1 and n inclusive.
    Recall that the nth square number is defined to be n*n.

    >>> squares(1)
    [1]
    >>> squares(2)
    [1, 4]
    >>> squares(3)
    [1, 4, 9]
    >>> squares(10)
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    '''
    squareslist = range(1, n+1)
    squareslist = map(lambda x: x**2, squareslist)
    return list(squareslist)


def lengths(strings):
    '''

    >>> lengths([])
    []
    >>> lengths(['test'])
    [4]
    >>> lengths(['this','is','a','test'])
    [4, 2, 1, 4]
    '''
    return list(map(lambda x: len(x), strings))

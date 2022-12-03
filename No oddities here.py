'''Write a small function that returns the values of an array that are not odd.

All values in the array will be integers. Return the good values in the order they are given.'''

def no_odds(values):
    res = []
    for i in values:
        if not i % 2:
            res.append(i)
    return res


def no_odds2(values):
    return [i for i in values if not i % 2]
    
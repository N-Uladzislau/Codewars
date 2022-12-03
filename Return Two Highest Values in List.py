'''
In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.

The result should also be ordered from highest to lowest.

Examples:

[4, 10, 10, 9]  =>  [10, 9]
[1, 1, 1]  =>  [1]
[]  =>  []
'''
def two_highest(arg1):
    if len(arg1) < 2:
        return arg1
    if arg1[0] > arg1[1]:
        max1 = arg1[0]
        max2 = arg1[1]
    else:
        max1 = arg1[1]
        max2 = arg1[0]
    for element in arg1[2:]:
        if element > max1:
            max2 = max1
            max1 = element
        elif element > max2 and element != max1:
            max2 = element
    return [max1, max2]


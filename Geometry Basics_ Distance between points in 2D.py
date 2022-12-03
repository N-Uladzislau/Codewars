'''
This series of katas will introduce you to basics of doing geometry with computers.

Point objects have x and y attributes (X and Y in C#) attributes.

Write a function calculating distance between Point a and Point b.

Tests round answers to 6 decimal places.
'''

import math 
def distance_between_points(a, b):
    p = [a.y, a.x]
    j = [b.y, b.x]
    return math.dist(p, j)
# short 
    return math.dist([a.x, a.y], [b.x, b.y])

# without math.dict
    return math.sqrt((a.x - a.y)**2 + (b.x - b.y)**2)

  



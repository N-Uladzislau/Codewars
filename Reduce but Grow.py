'''
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
'''
# simple 
def grow(arr):
    new = 1
    for i in arr:
        new *= i
    return new
  
# with reduce -> take two paraments and by seq * each number in arr 
from functools import reduce
def grow(arr):
    return reduce(lambda x, y: x * y, arr):
  
    
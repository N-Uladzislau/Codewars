# reduce(function(x,y), interable) -> value 
# sequence for each value and return one value 
from functools import reduce
l = [1, 4, 6, 7] # 1 - 4 - 6 - 7
print(reduce(lambda x, y: x - y, l)) # -> -16
# reduce(func, seq)


# own reduce func 
def grow2(arr):
    return myreduce(lambda x, y: x * y, arr)
# seq = [1, 2, 3, 4]
#          [2, 3, 4]
#              [6,4]
#               [24]
def myreduce(func, seq):
    if len(seq) == 0:
        return None
    if len(seq) == 1:
        return seq[0]
    result = seq[0]
    for el in seq[1::]:
        result = func(result, el)
    return result
  
def reduce(fucntion, iterable, initializer=None):
  it = iter(iterable)
  if initializer is None:
    value = next(it)


print(reduce(lambda x,y: x + str(y), [1,2,3,4], "s")) -> # return s1234
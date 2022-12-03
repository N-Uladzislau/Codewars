'''Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).'''

# looking for odd number 
def find_it(seq):
    d = {}  
    for num in seq:
        if d.get(num) is not None:
            d[num] += 1
        else:
            d[num] = 1
    return list(filter(lambda x: d[x] % 2, d))[0]
# best EX
def find_it2(seq):
  d = {}
  for num in seq:
      if d.get(num) is not None:
          d[num] += 1
      else:
          d[num] = 1
  return next(filter(lambda x: d[x] % 2, d)) # next -> return fist el of iteration 

# word Longer than usually 
  # count makes second iteration 
def find_it3(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
      
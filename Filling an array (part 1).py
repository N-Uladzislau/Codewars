'''
We want an array, but not just any old array, an array with contents!
Write a function that produces an array with the numbers 0 to N-1 in it.
For example, the following code will result in an array containing the numbers 0 to 4:
arr(5) // => [0,1,2,3,4]
Note: The parameter is optional. So you have to give it a default value.
'''
# arr(5) // => [0,1,2,3,4]
def arr(n=0): 
    return [i for i in range(n)] if n else []

def arr1(n=0):
    return list(range(n))

def arr(n=0): 
    result = []
    for i in range(n):
        result.append(i)
    return result

def arr(n=0):
  result = []
  i = 0
  while i < n:
    result.append(i)
  return result
  
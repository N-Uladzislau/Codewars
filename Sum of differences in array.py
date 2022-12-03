'''Your task is to sum the differences between consecutive pairs in the array in descending order.
Example
[2, 1, 10]  -->  9
In descending order: [10, 2, 1]
Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9
If the array is empty or the array has only one element the result should be 0 (Nothing in Haskell, None in Rust).'''

# math solving if we take first and last el in arr and subtraction
# it's gonna be like in exam below 
def sum_of_differences(arr):
    if len(arr) <= 1:
        return 0    
    arr.sort(reverse=True)
    return arr[0] - arr[-1]
# bad example 'cause sort() method -> will call many times and your code it's take more time and data 
def sum_of_differences2(arr):
    if len(arr) <= 1:
        return 0
    arr.sort(reverse=True)
    sum = 0
    for i in range(1, len(arr)):
        sum += arr[i - 1]- arr[i]
    return sum

# instead sort()
def sum_of_differences1(arr):
  if len(arr) <= 1:
    return 0
  return max(arr) - min(arr)

# one line 
def sum_of_differences(arr):
     return  0 if len(arr) <= 1 else max(arr) - min(arr)
    
'''
Write a function that takes a positive integer n, sums all the cubed values from 1 to n, and returns that sum
Assume that the input n will always be a positive integer.
Examples: (Input --> output)
2 --> 9 (sum of the cubes of 1 and 2 is 1 + 8)
3 --> 36 (sum of the cubes of 1, 2, and 3 is 1 + 8 + 27)
'''
# 
def sum_cubes(n):
    result = 0
    for i in range(1, n+1):
        result += i**3 
    return result

def sum_cubes2(n):
    return sum(i**3 for i in range(0,n+1))
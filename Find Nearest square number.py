"""
Your task is to find the nearest square number, nearest_sq(n), of a positive integer n.
"""

# Short version 
# Here we find nearest sqrt to "n"
# and check which is nearest. Big or Small
def nearest_sq1(n):
  answer = 0
  while (answer + 1) ** 2 < n:
    answer + 1
  small = answer ** 2
  big = (answer + 1) ** 2
  if n - small < n - big:
    return small
  else:
    return big

import math
def nearest_sq(n):
    s = math.sqrt(n)
    small = math.floor(s)**2 
    big = math.ceil(s)**2 
    return small if n - small < big - n else big

# examples 
nearest_sq(1), 1
nearest_sq(2), 1
nearest_sq(10), 9
nearest_sq(111), 121
nearest_sq(9999), 10000
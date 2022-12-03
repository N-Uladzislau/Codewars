'''Finish the solution so that it takes an input n (integer) and returns a string that is the decimal representation of the number grouped by commas after every 3 digits.

Assume: 0 <= n < 2147483647

Examples
       1  ->           "1"
      10  ->          "10"
     100  ->         "100"
    1000  ->       "1,000"
   10000  ->      "10,000"
  100000  ->     "100,000"
 1000000  ->   "1,000,000"
35235235  ->  "35,235,235"'''
# add "," to number 

import math
def group_by_commas(n):
    res = ""
    count = 0
    while n > 0: 
        if count == 3: 
            res = "," + res # add ',' to res 
            count = 0
        res = str((n % 10)) + res # n % 10 and make it str left without last numb 
        n = math.floor(n // 10) 
        count += 1
    return res
    
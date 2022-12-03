"""
Return a new array consisting of elements which are multiple of their own index in input array (length > 1).
"""
# Some cases:
"""
[22, -6, 32, 82, 9, 25] =>  [-6, 32, 25]

[68, -1, 1, -7, 10, 10] => [-1, 10]

[-56,-85,72,-26,-14,76,-27,72,35,-21,-67,87,0,21,59,27,-92,68] => [-85, 72, 0, 68]
"""
# enumerate -  arr 
# take index and value 
# reminder value on index :
# we cannot divide by 0:
# if index == 0: 
# continue 
def multiple_of_index(arr):
    result = []
    for index, value in enumerate(arr):
        if index == 0:
            continue
        if value % index == 0:
            result.append(value)
    return result

  
# another with exception
# allows us divide by 0 
# pass command: DO NOTHING - just continue 
def multiple_of_index(arr):
    result = []
    for index, value in enumerate(arr):
      try:
        if value % index == 0:
          result.append(value)
      except ZeroDivisionError:
        pass # continue works either
    return result

# 3rd example 
# index != 0: except 0
def multiple_of_index(arr):
    result = []
    for index, value in enumerate(arr):
        if index != 0 and value % index == 0:
          result.append(value)
    return result

  
# short version in one line 
def multiple_of_index(arr):
  # [ ] - means we create list and return list 
  # create 
  return [value for index, value in enumerate(arr) if index != 0 and value % index == 0]
  
multiple_of_index([22, -6, 32, 82, 9, 25]), [-6, 32, 25])
multiple_of_index([68, -1, 1, -7, 10, 10]), [-1, 10])
multiple_of_index([11, -11]), [-11])
multiple_of_index([-56,-85,72,-26,-14,76,-27,72,35,-21,-67,87,0,21,59,27,-92,68], [-85, 72, 0, 68])
multiple_of_index([28,38,-44,-99,-13,-54,77,-51]), [38, -44, -99])
multiple_of_index([-1,-49,-1,67,8,-60,39,35]), [-49, 8, -60, 35])




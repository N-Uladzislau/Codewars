'''Some really funny web dev gave you a sequence of numbers from his API response as an sequence of strings!
You need to cast the whole array to the correct type.
Create the function that takes as a parameter a sequence of numbers represented as strings and outputs a sequence of numbers.
ie:["1", "2", "3"] to [1, 2, 3]
Note that you can receive floats as well.'''

# ["1.1", "2.2", "3.3"]) -> [1.1, 2.2, 3.3]
def to_float_array(arr): 
    return list(map(lambda x: float(x), arr))


import numpy as np
def to_float_array2(arr):
    return np.asarray(arr, dtype=float)


def to_float_array3(arr):
    return [float(n) for n in arr]
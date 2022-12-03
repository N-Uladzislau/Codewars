def array_diff(a, b):
    b = set(b) # optimization on data - > set hasn't duplicate 
    return list(filter(lambda el: el not in b ,a))

array_diff([1,2], [1]) # return - > [2]
array_diff([1,2,2,2,3],[2]) # return ->  [1,3]


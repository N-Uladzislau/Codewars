from functools import reduce
import operator
print(reduce(operator.mul, [1,2,3,4]))
print(reduce(operator.add, [1,2,3,4]))
print(reduce(operator.floordiv, [1,2,3,4]))

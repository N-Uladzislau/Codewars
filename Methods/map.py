# l = [0, 1, 2, 3, 4] ->  ["0", "1", "2", "3", "4"]
# map(fucntion(x), interable) -> interable
# instead
srow = ','.join([str(value) for value in row])
# simpler 
srow = ",",join(map(str, row)) # [0, 1, 2, 3, 4] ->  ["0", "1", "2", "3", "4"]

row = [1,2,3,4]
print(list(map(str, row))) [# ->  ["1", "2", "3", "4"]

# Return list with ...
print(list(map(lambda x: x **2, row)))

a = '12345'
print(list(map(int, a)))# -> [1,2,3,4,5]

def increase(v):
  return v + 1
print(list(map(increase, a)) # return [2,3,4,5,6]

CODES ='''\
1-kiwi
2-pear
3-kiwi
4-banana'''.splitlines()
# ['1-kiwi', '2-pear', '3-kiwi', '4-banana']
CODES = map(lambda line: line,split('-'), CODES)
print(list(CODES)) -> return [['1', 'kiwi'], ['2', 'pear'], ['3' 'kiwi'], ['4', "banana"]]
# Takes one first el 
CODES = map(lambda line: line,split('-')[1], CODES)
print(list(CODES)) -> return ['kiwi'], ['pear'], ['kiwi'], ["banana"]

arr = ["1.1", "2.2", "3.3"]
return list(map(lambda x: float(x), arr)) # ["1.1", "2.2", "3.3"]) ->  [1.1, 2.2, 3.3]



      
      
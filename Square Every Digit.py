'''
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
Note: The function accepts an integer and returns an integer
'''
def square_digits(num):
    result = ""
    for x in str(num):
        result += str(int(x)**2)
    return int(result)

# weird but works 
def square_digits2(num):
    z = map(int, str(num))
    
    xxx = list(map(lambda x: x ** 2 , z))
    
    return int(''.join(map(str,xxx)))

def square_digits3(num):
    return int("".join([str(int(d) **2) for d in str(num)]))


square_digits(9119)

"""
9119 => "9119" => "9", "1", "1", "9" => 9, 1, 1, 9 =>
9 ** 2 => 81
1 ** 2 => 1
1 ** 2 => 1
9 ** 2 => 81
= > "811181"
"""
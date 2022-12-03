'''
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]
'''
def digitize(n):
    return list(map(int,str(n)[::-1]))


def digitize2(n):
    x = list(map(int, str(n)))
    x.reverse()
    return x

def digitize1(n):
    if not n:
        return [0]
    res = []
    while n:
        res.append(n % 10)
        n //= 10
    return res
  

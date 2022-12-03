'''If you can't sleep, just count sheep!!
Task:
Given a non-negative integer, 3 for example, return a string with a murmur: 
Input will always be valid, i.e. no negative integers.'''
#"1 sheep...2 sheep...3 sheep...". 

def count_sheep(n):
    sheep = ''
    for i in range(1, n + 1):
        sheep += f"{i} sheep..."
    return sheep


def count_sheep(n):
    result = ""
    for i in range(n):
        result += f"{i+1} sheep..."
    return result

  
def count_sheep2(n):
    return [f"{i+1} sheep..." for i in range(n)]


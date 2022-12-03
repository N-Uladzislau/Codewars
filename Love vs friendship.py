'''
If　a = 1, b = 2, c = 3 ... z = 26
Then l + o + v + e = 54
and f + r + i + e + n + d + s + h + i + p = 108
So friendship is twice as strong as love :-)
Your task is to write a function which calculates the value of a word based off the sum of the alphabet positions of its characters.
The input will always be made of only lowercase letters and will never be empty.
'''
DICT = {chr(i+96):i for i in range(1,27)}
def words_to_marks(s):
    result = 0
    for c in s:
        result += DICT[c] 
    return result
# short
    return sum(DICT[c] for c in s)
  
# letter to number minus 96 and get our word 
def words_to_marks(s):
    return sum(ord(c) - 96 for c in s) 

'''
Help the frog to find a way to freedom
You have an array of integers and have a frog at the first position

[Frog, int, int, int, ..., int]

The integer itself may tell you the length and the direction of the jump

For instance:
 2 = jump two indices to the right
-3 = jump three indices to the left
 0 = stay at the same position
Your objective is to find how many jumps are needed to jump out of the array.

Return -1 if Frog can't jump out of the array

Example:
array = [1, 2, 1, 5]; 
jumps = 3  (1 -> 2 -> 5 -> <jump out>)
'''
def solution(a: list) -> int:
    # jumps  [1, 2, 2, -1] jump      position jump_counter
    # 0      [*,  ,  ,   ]           0        0
    # 1      [ , *,  ,   ] 1  /1     1        1
    # 2      [ ,  ,  ,  *] 2  /2     3        2
    # 3      [ ,  , *,   ] -1 /2     2        3
    # 4      [ ,  ,  ,   ] 2  /-1    4        4
    
    jump_counter = 0                                # set jump counter to 0
    position = 0                                    # set frog position to 0
    for i in range(len(a)):                         # while not repeating
        jump = a[position]
        position += jump                            # add specified jump to frog position
        jump_counter += 1                           # increase jump counter
        if position < 0 or position > len(a) - 1:   # if frog position isn't in a range
            return jump_counter                     # then return jump counter
    return -1
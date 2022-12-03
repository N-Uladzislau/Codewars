'''Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
Examples input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false'''

def xo(s):
    nx = 0
    no = 0
    for i in s.lower():
        if i == "x":
            nx += 1
        if i == "o":
            no += 1
    return nx == no


  # not res return True -> else False 
  # count our res -> should be 0 if not False
def xo2(s):
    res = 0
    for i in s.lower():
        if i == "x":
            res += 1
        if i == "o":
            res -= 1
    return not res

# count our words in list 
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o').lower
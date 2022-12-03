'''
Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. For a beginner kata, you can assume that the input data is always a non empty string, no need to verify it.

remove("Hi!") === "Hi!"
remove("Hi!!!") === "Hi!"
remove("!Hi") === "Hi!"
remove("!Hi!") === "Hi!"
remove("Hi! Hi!") === "Hi Hi!"
remove("Hi") === "Hi!"
'''
def remove(s):
  new = [x for x in s if x != "!"]
  list = ["!"]
  result = new + list
  return "".join(result)
# short 
  return  "".join([x for x in s if x != "!"]) + "!"

# easyest 
def remove1(s):
    return s.replace("!", "") + "!"
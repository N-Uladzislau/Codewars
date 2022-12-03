"""Basic regex tasks. Write a function that takes in a numeric code of any length. The function should check if the code begins with 1, 2, or 3 and return true if so. Return false otherwise.

You can assume the input will always be a number."""


def validate_code2(code):
# valid    return int(str(code)[0]) < 4
    return str(code)[0] < "4"

# 
def validate_code(code):
  # startsWith can take tuple and take several arguments 
  return str(code).startswith(("1", "2", "3"))


def validate_code(code):
    for i in str(code):
      new = int(i)
      if new == 1 or new == 2 or new == 3:
          return True
      else:
          return False
        
# find number in string 
def validate_code(code):
  return str(code)[0] in '123'


validate_code(123), True)
validate_code(248), True)
validate_code(8), False)
validate_code(321), True)
validate_code(9453), False)

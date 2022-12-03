# Create a function that returns the,
# CSV representation of a two-dimensional numeric array.

'''
input:
   [[ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]] 

'''
# short version 
def to_csv_text(array):
  return '\n'.join(
    [','.join([str(value) for value in row])
    for row in array]
  )
  # long 
def to_csv_text(array):
  rows = []
  for row in array:
    # l = [0, 1, 2, 3, 4] ->  ["0", "1", "2", "3", "4"]
    srow = ','.join([str(value) for value in row])
    rows.append(srow)
  return '\n'.join(rows)

# with map 
def to_csv_text(array):
  return "\n".join([','.join(map(str, row)) for row in array])

def to_csv_text(array):
  rows = []
  for row in array:
    rows.append(','.join(map(str, row)))
  return '\n'.join(rows)
  


assert_equals(
to_csv_text([
[0, 1, 2, 3, 45],
[10, 11, 12, 13, 14],
[20, 21, 22, 23, 24],
[30, 31, 32, 33, 34]
]),
"0,1,2,3,45\n10,11,12,13,14\n20,21,22,23,24\n30,31,32,33,34",
)
assert_equals(
to_csv_text([
[-25, 21, 2, -33, 48],
[30, 31, -32, 33, -34]
]),
"-25,21,2,-33,48\n30,31,-32,33,-34",
)
test.assert_equals(
to_csv_text([
[5, 55, 5, 5, 55],
[6, 6, 66, 23, 24],
[666, 31, 66, 33, 7]
]),
"5,55,5,5,55\n6,6,66,23,24\n666,31,66,33,7",
)
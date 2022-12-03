# Find number 6 : multply or disctructs number in array to GET 6 ! ! ! 


# Bad example 
arr = [1, 2, 4, 6, 0, 7, -1, 5]
n = 6
# (0,7), (1,2), (3, 4), (5, 6)
def find_pairs(s, ls): 
  res = [] # - > create empty list 
  
  for i in range(len(ls)): # -> go through list -> 
    for x in range(i + 1, len(ls)): # -> go through list again from index i + 1 : index 1 
      if ls[i] + ls[x] == s: # Check if i and x in ls  == 6 
        res.append((i, x)) # add to our list 
  return res
print(find_pairs(n, arr)) 


# Good EX
def find_pairs_2(s, ls):
  res = []
  tab = {}
  for i in range(len(ls)):
    tab[ls[i]] = i

  for i in range(len(ls)):
    el = tab.get(s - ls[i])
    if el and el != i:
      res.append((i, el))
      tab.pop(ls[i], None)
      
  return res
print(find_pairs_2(n, arr)) 
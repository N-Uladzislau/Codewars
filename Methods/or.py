def f(x): 
  return x or [7,7,7] # if we call func and argument is None -> return [7,7,7]
print(f([1]))
print(f([])) -> # return [7,7,7]





def z(x):
  m = max(x or [-1]) 
  return m

print(z([1])) return 1 
print(z([])) return -1 

def f(x):
  if not x:

    return f'[{x}]'
    
    return f"[{x if x else 'ops'}]"

    return f"[{x or 'ops'}]"

    
print(f('abc'))  return -> "abc"
print(f('')) return -> 'ops'


a = [True, True, True]
print(any(a)) -> # True 
print(all(a)) -> # True 


l = [True, True, False]
print(any(l)) -> # True 
print(all(l)) -> # False


l = [False, False]
print(any(l)) -> # False 
print(all(l)) -> # False

# any() -> check if one of el is True -> return True -> Else False 
# all() -> check if all el is True -> return True -> Else False


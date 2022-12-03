'''
Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105
'''
def no_boring_zeros(n):
    s = str(n).rstrip("0")
    return int(s) if n != 0 else 0

def no_boring_zeros2(n):
    new = str(n)
    new1 = int(new.rstrip("0")) if n != 0 else 0
    return new1
    
    return int(str(n).rstip("0") if n != 0 else 0)
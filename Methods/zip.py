p = "ąćęłńóśźż"
l = "acelnoszz"
print(list(zip(p,l))) # return ->  [('ą','a'), ("ć", "c")] 

arr = [10, 2, 1, 4]
# arr[1:] = [4, 2, 1]
# zip(arr, arr[1:]) = [(10, 4), (4, 2), (2,1)]
print(sum(a - b for a, b in zip(arr, arr[1:])))
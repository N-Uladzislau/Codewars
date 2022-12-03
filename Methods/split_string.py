print('''
abc
def
''').split('\n') -> return ['', 'abc', 'def', '']

print('''\
abc
def\
''').split('\n') return -> ['abc', 'def'] "\" ->  makes in one line 

splitlines() -> 'method splits a string into a list. The splitting is done at line breaks'

# makes new line instead '\n' -> use splitlines()
print('''
abc
def
'''.splitlines()) -> return ['', 'abc', 'def', '']
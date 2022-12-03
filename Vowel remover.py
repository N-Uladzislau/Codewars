'''
Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.
Examples
"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"
don't worry about uppercase vowels
y is not considered a vowel for this kata
'''
VOWELS = ("a", "e", "i", "o", "u" )
def shortcut( s ):
    return "".join(i for i in s if i not in VOWELS)

  # With tuple through replace -> replace take two arguments : 
X = [("a", ""),('e', ''),("i", ''),('o',''), ('u','')]
def shortcut1( s ):
    for char, replace in X:
        if char in s:
            s = s.replace(char, replace)
    return s

# with string in replace 
def shortcut2(s):
    for i in "aeiou":
        s = s.replace(i, '')
    return s


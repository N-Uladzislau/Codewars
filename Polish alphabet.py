'''
There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants.
Your task is to change the letters with diacritics:
ą -> a,
ć -> c,
ę -> e,
ł -> l,
ń -> n,
ó -> o,
ś -> s,
ź -> z,
ż -> z
and print out the string without the use of the Polish letters.
For example:
"Jędrzej Błądziński"  -->  "Jedrzej Bladzinski"
'''
DICT = {
    'ą': 'a',
    "ć":"c",
    "ę":"e",
    "ł":"l",
    "ń":"n",
    "ó":"o",
    "ś":"s",
    "ź":"z",
    "ż":"z"
} # use items with Dictionaty
def correct_polish_letters(st):
    for key, value in DICT.items():
        st = st.replace(key, value)
    return st 

# use zip()
def correct_polish_letters1(st):
    p = "ąćęłńóśźż"
    l = "acelnoszz"
    for key, value in zip(p, l): # return ->  [('ą','a'), ("ć", "c")] 
        st = st.replace(key, value)
    return st
  
def correct_polish_letters2(st):
  p = "ąćęłńóśźż"
  l = "acelnoszz"
  for i in range(len(p)):
    key = p[i]
    value = l[i]
    st = st.replace(key, value)
  return st
  # short 
    st = st.replace(p[i], l[i])
  return st
  
  
    

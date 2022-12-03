# Change symlols 
def correct_polish_letters(st):
  return st.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))

# change
print("abcde".translate(str.maketrans('abc', "ABC"))) -> # return ABCde

# deleting 
print("abcde".translate(str.maketrans('', '', "abc")) -> # return de

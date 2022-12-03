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
}
def correct_polish_letters(st):
  for key, value in DICT.items(): # return -> [('ą','a'), ("ć", "c")] 
    st = st.replace(key, value)
  return st
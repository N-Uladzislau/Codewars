'''
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
'''
def get_grade(s1, s2, s3):
    avg = (s1+s2+s3) // 30
    if 9 <= avg:
        return 'A'
    if 8 <= avg:
        return 'B'
    if 7 <= avg:
        return 'C'
    if 6 <= avg:
        return 'D'
    else:
        return 'F'
# Through list
def get_grade1(s1, s2, s3):
  avg = (s1+s2+s3) // 30
  grades = ["F","F","F","F","F","F","D","C","B","A","A"]
  return grades[avg]
# Througn string
def get_grade2(s1, s2, s3):
  avg = (s1+s2+s3) // 30
  grades = 'FFFFFFDCBAA'
  return grades[avg]
  # short
  return 'FFFFFFDCBAA'[(s1 + s2 + s3) // 30]
  # dictinary
  return {6:"D", 7:"C",8:"B",9:"A",10:"A"}.get((s1+s2+s3) / 30, "F")
      
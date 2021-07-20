student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades ={}

for i in student_scores:
  score = student_scores[i]
  if score>90:
    student_grades[i] = "Outstanding"
  elif score >80:
    student_grades[i] = "Exceeds Expectation"
  elif score>70:
    student_grades[i] = "Acceptable"
  else:
    student_grades[i] = "Fail"

print(student_grades)






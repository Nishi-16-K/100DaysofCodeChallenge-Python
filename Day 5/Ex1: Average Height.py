student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#print(student_heights)

sum_of_heights = 0
total_num = 0
for total in student_heights:
  sum_of_heights= sum_of_heights + total

for student in student_heights:
  total_num = total_num+1

avg_height = sum_of_heights/total_num
print(round(avg_height))

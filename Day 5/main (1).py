# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height=0
for height in student_heights :
  total_height+=height

total_students=0
for students in student_heights :
  total_students+=1

print(f'Average height of students is {total_height/total_students}')





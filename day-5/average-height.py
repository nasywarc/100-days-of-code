# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

total_height = 0
number_of_student = 0

for i in student_heights:
    total_height += i
    number_of_student += 1


print(f"total height {total_height}")
print(f"number of students {number_of_student}")
print(f"average height ")

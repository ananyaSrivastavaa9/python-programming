# Creating a list of students
students = ['Alice', 'Bob', 'Charlie']
num = [1,9,6,3,0]

num.sort()
print(num)

# Adding a new student
students.append('David')  # ['Alice','Bob','Charlie','David']

# Removing a student
students.remove('Bob')     # ['Alice','Charlie','David']

# Accessing students by index
print(students[0])  # Alice
print(students[1])  # Charlie

# Slicing first two students
print(students[0:2])  # ['Alice','Charlie']

# inserting
students.insert(0,"anu")
print(students)

# pop
students.pop()
print(students)
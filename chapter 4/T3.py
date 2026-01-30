# accept marks of 6 students and display them in sorted manner
marks = []
for i in range(6):
    m = int(input("enter marks: "))
    marks.append(m)
marks.sort()
print(marks)
# basic for syntax
marks = [4,7,9,2,"ananya",True]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

# negative indexing
print(marks[-3]) #negative
print(marks[len(marks)-3]) #positive
print(marks[6-3])
print(marks[3])

# check whether item present or not
if "ananya" in marks:
    print("yes")
else:
    print("no")

if "ya" in "ananya":
    print("yes")
else:
    print("no")

# range
print(marks)
print(marks[:])
print(marks[1:-1])
print(marks[1:len(marks)-1])
print(marks[1:4:2])

# list comprehension
lst = [i for i in range(4)]
print(lst)

lst = [i*i for i in range(4) if i%2==0]
print(lst)

name = ["milo", "sarah", "bruno", "rosa"]
namewith_o = [item for item in name if "o" in item]
print(namewith_o)
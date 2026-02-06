# If the names of 2 friends are same; what will happen to the program in problem 
# 6? 

a = {}
a["Ravi"] = "Python"
a["Ravi"] = "Java"
print(a)

# If two friends have the same name,
# the latest value will overwrite the previous one 
# because dictionaries do not allow duplicate keys.
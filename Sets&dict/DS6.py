# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 

a = {}
for i in range(4):
    key = input("enter names : ")
    values = input("enter fav language : ")
    a[key] = values
print(a)
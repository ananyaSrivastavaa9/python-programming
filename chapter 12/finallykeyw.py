# finally clause
try:
    l = [1,2,3,4]
    i = int(input("enter the index no: "))
    print(l[i])
except:
    print("some error occurred")

finally:
    print("I am always executed")
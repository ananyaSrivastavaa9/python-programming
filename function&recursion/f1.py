# function 1
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

# function 2
def isGreater(a,b):
    if(a>b):
        print("first number is largest")
    else:
        print("Second number is largest")

a = 10
b = 8
calculateGmean(a,b) #function call
isGreater(a,b) #function call

c = 5
d = 11
calculateGmean(c,d) #function call
isGreater(c,d) #function call
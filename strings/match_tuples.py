point = (0,1)
match point:
    case (0,1):
        print("Same value")
    case (0,y):
        print("the value of y = ", y)
    case (x,0):
        print("the value of x = ", x)
    case (x,y):
        print("point at : ", x, y)
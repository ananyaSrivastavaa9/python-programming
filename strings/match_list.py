value = [1,2]
match value:
    case [1,2]:
        print("same value")
    case [x,y]:
        print("value of x and y are : ", x, y)
    case [0,y]:
        print("value of y is ", y)
    case [x,0]:
        print("value of x is ", x)
    case _:
        print("invalid")
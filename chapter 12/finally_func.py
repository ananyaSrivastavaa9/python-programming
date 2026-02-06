def func2():
    l = [10,20,30,40]
    try:
        i = int(input("enter index no: "))
        print(l[i])
        return 1
    except (ValueError, IndexError):
        print("Invalid index")
        return 0
    finally:
        print("execution completed")
a = func2()
print(a)
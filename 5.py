# import time
# print(time.strftime('%H:%M:%S'))
x=int(input("enter the x value"))
match x:
    case 0:
        print("x is 0")
    case 4:
        print("x is 4")
    case _ if x!=90:
        print("x is not 90")


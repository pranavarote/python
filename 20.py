# a=input("enter the number")
# print(f"multipliication table of {a}is :")
# try:
#   for i in range(1,11):
#     print(f"{int(a)} X {i} ={int(a)*i}")
# except Exception as e :
#     print("invalid input")
# print("some imp lines of the code")
# print("end of the code")

try:
    num=int(input("enter a number"))
    a=[2,4,5]
    print(a[num])
except Exception as e:
    print(e)



# # for loop
# name="shantaram"
# for i in name:
#     print(i)
#     if(i=="r"):
#         print("yhis is something special")
#
# colors=["green","yellow","red","blue"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)
# for k in range(1,100,10):
#     print(k+1)

# while loop
# i=int(input("enter the number"))
# while (i<=23):
#     i=int(input("enter the number"))
#     print(i)
# print("done with the loop")
# i=0
# while(i<10):
#     print(i)
#     i=i+1

######

# i=4
# while(i>0):
#     print(i)
#     i=i-1
#
# else:
#     print("i am outsidethe loop")


# do while loop
secret_word = "python"
counter = 0

while True:
    word = input("Enter the secret word: ").lower()
    counter = counter + 1
    if word == secret_word:
        break
    if word != secret_word and counter > 7:
        break
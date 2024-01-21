import time
t=time.strftime('%H:%M:%S')
print(t)
hour=int(time.strftime('%H'))
print(hour)
hour=23
if(hour >0 & hour<12):
    print("good morning sir")
elif(hour>12 & hour<16):
    print("good afternoon sir")
elif(hour>17 and hour<0):
    print("good night sir!")



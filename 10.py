# tuple
tup=(1,2,3,4,5,6,7,8,9,0)
print(type(tup))
print(tup)
print(tup[4])
print(tup[-5])
print(tup[-3])
print(len(tup))
if 54 in tup:
    print("yes this number is present in the tuple")
else:
    print("no,this number is not present in the tuple")
    tup2 =tup [1:5]
    print(tup2)

# operations on tuple
countries=("india","grmany","russia","america","england")
print(type(countries))
temp=list(countries)
print(type(temp))
temp.append("ukrain")

temp.pop(4)
temp[2]="finland"
countries=tuple(temp)
print(type(countries))
print(countries)
print(countries.count("india"))
tup=(1,2,3,44,23,45,3,2,1,54,57)
print(tup.index(3,4,8))
print(len(tup))
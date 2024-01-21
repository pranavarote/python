# A dictionary in Python is a data structure that stores the value in value:key pairs.
#
# Example:
#
# As you can see from the example, data is stored in key:value pairs in dictionaries, which makes it easier to find values.
#
# Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# print(Dict)

dict ={'harry':'human being',"pranav":"engineer","college":"vppcoe",1:"raj"}
print(type(dict))
print(dict["harry"])
print(dict[1])

print(dict.values())
print(dict.items())
for key,value in dict.items():
    print(f"th values correspondings to the the {key} is {value} ")

# methods of dctionary
a={1:'pranav',2:'raj',3:'ujjwal',4:'harsh',5:'gaurav',6:'sitaram'}
b={7:'prajkata',8:'manisha',9:'baban'}
a.update(b)
print(a)
a.clear()
print(a)
a.pop(4)
print(a)
a.popitem()
del b
print(a)
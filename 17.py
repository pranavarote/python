# # sets
#
# A Set in Python programming is an unordered collection data type that is iterable, mutable and has no
# duplicate elements.
#
# Set are represented by { } (values enclosed in curly braces)
#
# The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for
# checking whether a specific element is contained in the set. This is based on a data structure known
# as a hash table. Since sets are unordered, we cannot access items using indexes as we do in lists.

s={1,2,3,4,5,67,5}
print(s)
info={"carla",23,False,432,"tesla",4.33}
print(info)
print(type(s))
for value in info:
    print(value)
g={}
print(type(g))

# methods of set
s1={1,2,3,4,5,6}
s2={23,45,1,5,6,3,8,7}
print(s1.union(s2))
print(s1.intersection(s2))
s1.update(s2)
s3=s1.difference(s2)
print(s3)
print(s1)
s4={1,2,3,4,5,6}
s5={23,45,1,2,5,4,6,3,8,7}
s6=s5.issuperset(s4)
print(s6)
s5.discard(45)
print(s5)
del s4


if "carla" in info:
    print("carla is present in info")
else:
    print("not present in info")
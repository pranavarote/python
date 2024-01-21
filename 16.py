# recursion
# The term Recursion can be defined as the process of defining something in terms of itself.
# In simple words, it is a process in which a function calls itself directly or indirectly.
# Advantages of using recursion
#
# A complicated function can be split down into smaller sub-problems utilizing recursion.
# Sequence creation is simpler through recursion than utilizing any nested iteration.
# Recursive functions render the code look simple and effective.
def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))
print(factorial(3))
print(factorial(5))
print(factorial(6))


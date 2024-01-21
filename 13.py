# String formatting allows you to create dynamic strings by combining variables and values.
# In this article, we will discuss about 5 ways to format a string.
#
# You will learn different methods of string formatting with examples for better understanding.
# Let’s look at them now!
#
# How to Format Strings in Python
# There are five different ways to perform string formatting in Python
#
# Formatting with % Operator.
# Formatting with format() string method.
# Formatting with string literals, called f-strings.
# Formatting with String Template Class
# Formatting with center() string method.
letter="my name is {0} .i am from {1}"
name="pranav"
country="india"
print(letter.format(name,country))
print(f"my name is {name}.i am from {country}")
price =12.45678
txt=f"for only {price:.2f} dollors"
print(txt.format(price=12.123456789))
print(txt)
# use double curly braces in you want to display the braces  in the string
s=f"he my name is {{raj}}"
print(s)
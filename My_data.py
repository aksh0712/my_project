import random
from pyexpat import model
from typing import Set

print(random.randrange(1, 10))

x = int(1)  # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3
print(x, y, z)

x = float(1)  # x will be 1
y = float(2.8)  # y will be 2
z = float("3")  # z will be 3
print(x, y, z)

x = complex(1)  # x will be 1
y = complex(2.8)  # y will be 2
z = complex("3")  # z will be 3
print(x, y, z)

x = str("s1")  # x will be 's1'
y = str(2)  # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x, y, z)

# string literals
print("Hello")
print('Hello')

# String assign to a variable
a = 'hello World'
print(a)

# Multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# string a array
a = "Hello, World!"
print(a[8])

# slicing
a = "Hello, World!"
print(a[1:5])

# negative indexing
b = "Hello, World!"
print(b[-8:-4])

# string length
a = "Hello,World!"
print(len(a))

# strip method
a = "     Hello, World!   "
print(a.strip())  # returns "Hello, World!"

# lower case
a = "HELLO, WORld!"
print(a.lower())

# upper case
a = "Hello, World!"
print(a.upper())

# replace the characters
a = 'Hello, World!'
print(a.replace('l', 'J'))

# splits the strings
a = "HelloWorld!"
print(a.split("W"))

# check the string
txt = "The rain in Spain stays mainly in the plain"
x = "ma" not in txt
print(x)

# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# string format
age = 36
txt = "My name is John, I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {1} pieces of item {0} for {2} dollars."
print(myorder.format(quantity, itemno, price))

# escape character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# functions can return a boolean value
x = 200
print(isinstance(x, int))

x = 5

x <<= 3

print(x)

set1 = {"Apple", "banana", "cherry", "Apple"}
set2 = {1, 2, 3, 2}

set1.update(set2)
print(set1)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes,the model key is in thisdict")

x = thisdict["model"]
print(x)

thisdict["model"] = "honda"
print(thisdict)

for x in thisdict:
    print(x)

for x in thisdict.items():
    print(x)

a=10
b=20
if(a>b):
    print("b is greater than a")
elif(a==b):
    print("a is equal to b")
else:
   print("b is greater than a")


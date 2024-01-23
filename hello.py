# Ask user for their name
name = input("What is your name? ")
# say hello to the user
print("hello, " + name)

### comments are ignored by the interpreter
### they are used to explain what the code does
### they start with a # and go until the end of the line
"""
This is a multi-line comment that can be used to explain a block of code
"""
# strrings in python called str
"""
formating Strings : probably the most elegant way to use strings would be as follows:"
name = input("What is your name? ")
print(f"hello, {name}")
Notice the f in print(f"hello, {name}"). This f is a special indicator to python to treat this string a special way.
The curly braces are placeholders for the variables that will be inserted into the string.
"""
# more on strings
# you should never expect your user will cooperate as intended. Therefore, you will need to ensure that the input of your user is corrected or checked.
# it turns out that built into strungs is the ability remove whitespace from the beginning and end of a string.
# by utilizing the strip() method, you can remove the whitespace from the beginning and end of a string.
# for example:
#Ask the user for their name 
name = input("What is your name? ")
# Remove whitespace from the str
name = name.strip()
# print the output
print(f"hello, {name}")
#Returning this program , regradless of how many spaces you type before or after your name, the output will always be the same, it will strip off all the whitespace from the beginning and end of the string.
## using the title() method , it would title case the user's name
# Ask the user for their name
name = input("What is your name? ")
# Remove whitespace from the str
name = name.strip()
# capitalize the first letter of each word
name = name.title()
# print the output
print(f"hello, {name}")
### notice that you can modify your code to be more efficient by chaining the methods together.
# Ask the user for their name
name = input("What is your name? ").strip().title()
# print the output
print(f"hello, {name}")
#Integers or int 
# In ptyhon , an integer is referred to as an int .
## in the world of mathematics we are familiar with +,-,*,/ and % operators. That last operator % or modulo operator may not be very familiar to you.
### the modulo operator returns the remainder of a division operation.
# for example:
# 10 / 3 = 3.3333333333333335
# first we can declare a few variables
x = 1
y = 2
z = x + y
print(z)
# to make it more interactive we can use the input function.
x = input(" What's x?")
y = input(" What's y?")
z = x + y
print(z)
# notice that the output is 12 and not 3. This is because the input function returns a string.
# we can fix this by converting the input to an int.
x = input(" What's x?")
y = input(" What's y?")
z = int(x) + int(y)
print(z)
# now the output is 3. The use of the int() function converts the string to an int.
# we can further improve our program as follows:
x = int(input(" What's x?"))
y = int(input(" What's y?"))
print(x + y)
# This illustrats that you can run functions on functions . the most inner function is run first , and then the outer one is run. first, the input function is run , then the int function.
# Readability wins 
## when deciding on your approch to a coding task , remember that one could make a resonable argumenrt for many approches to the same problem.
### Regardless of what approch you take to a programming task, remember that readability wins.you should use comments to give yourself and others clues about what your code is doing and why. further, you should create code in a way that is readable and understandable.

# Float Basics
# A floating point value is a real number that has a decimal point in it , such as 0.52.
# for example:
x = float(input(" What's x?"))
y = float(input(" What's y?"))
print(x + y)
## lets imagine , however , that you want to round the total to the nearset integer . looking at python documanatuons for round(), you will see that the availablle arguments are round(number [n,ndigits]). 
# those square brackets indicate that something optinal can be specified by the programmer, therefore , you could do round(n)to round a digit to the nearest integer.
# for example:
# get the user's input
x = float(input(" What's x?"))
y = float(input(" What's y?"))

# create a rounded result
z = round(x + y)

# print the result
print(z)
# this will round the result to the nearest integer.

## what if we wanted to format the output of long numbers ? for example , rather than seeing 1000, you may wish to see 1,000.
# get the user's input
x = float(input(" What's x?"))
y = float(input(" What's y?"))
#create a rounded result
z = round(x + y)
# print the formatted result
print(f"{z:,}")
# this will format the number with a comma every three digits.

# More on Floats
# how can we round floating point values? first, modify your code as follows:
# get the user's input
x = float(input(" What's x?"))
y = float(input(" What's y?"))
# calculate the result
z = x / y
# print the result
print(z)
# whem inputing 2 as x and 3 as y , the output is 0.6666666666666666. 
# lets say we want to round this down :
# get the user's input
x = float(input(" What's x?"))
y = float(input(" What's y?"))
# calculate the result and round
z = round(x / y,2)
# print the result
print(z)
# this will round the result to two decimal places.
# we can also use fstrings to format the output:
# get the user's input
x = float(input(" What's x?"))
y = float(input(" What's y?"))
# calculate the result 
z = x / y
# print the result
print(f"{z:.2f}")


# Def 
## would it be nice to create our own function ? 
### ask the user for their name , remove whitespace , and capitalize the first letter of each word.
name = input("What is your name? ").strip().title()
#print the output
print(f"hello, {name}")
# we can better our code to create owr own special function that says " hello " for us"
# erasing all our code and starting over
name = input("What is your name? ")
#hello()
print(name)


# this will return an error because the function hello() is not defined.
# we can define a function as follows:
def hello():
    print("hello")
name = input("What is your name? ")
hello()
print(name)   

# this will print hello and then the name of the user.
# we can further improve our code:

## create our own function
def hello(to):
    print("hello," ,to)
## output using our own function
name = input("What is your name? ")
hello(name)

# We can change our code to add a default value to hello:

# Create our own function
def hello(to="world"):
    print("hello,", to)


# Output using our own function
name = input("What's your name? ")
hello(name)

# Output without passing the expected arguments
hello()

 # Test out your code yourself. Notice how the first hello will behave as you might expect and the second hello, which is not passed a value, will by default output hello, world.
# We don’t have to have our function at the start of our program. We can move it down, but we need to tell the compiler that we have a main function and we have a separate hello function.

def main():
# Output using our own function
    name = input("What's your name? ")
hello(name)
# Output without passing the expected arguments
hello()


# Create our own function
def hello(to="world"):
    print("hello,", to)
## This alone, however, will create an error of sorts. If we run python hello.py nothing happens! The reason for this is that nothing in this code is actually calling the main function and bringing our program to life.
 # The following very small modification will call the main function and restore our program to working order:

def main():

 # Output using our own function
    name = input("What's your name? ")
hello(name)
# Output without passing the expected arguments
hello()
# Create our own function
def hello(to="world"):
    print("hello,", to)
main()    


###Returning Values
# You can imagine many scenarios where you don’t just want a function to perform an action, but also to return a value back to the main function. For example, rather than simply printing the calculation of x + y, 
# you may want a function to return the value of this calculation back to another part of your program. This “passing back” of a value we call a return value.
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n

main()
#Effectively, x is passed to square. Then, the calculation of x * x is returned back to the main function.





### Conditionals
'''Conditionals allow you, the programmer, to allow your program to make decisions: As if your program has the choice between taking the left-hand road or the right-hand road based upon certain conditions.
Built within Python are a set of “operators” that can are used to ask mathematical questions.
> and < symbols are probably quite familiar to you.
>= denotes “greater than or equal to.”
<= denotes “less than or equal to.”
== denotes “equals, though do notice the double equal sign! A single equal sign would assign a value. Double equal signs are used to compare variables.
!= denotes “not equal to.
Conditional statements compare a left-hand term to a right-hand term.'''


### if statements
x = int(input("What's x? "))
y = int(input("What's y? "))
if x < y:
    print("x is less than y")
# Notice how your program takes the input of the user for both x and y, casting them as integers and saving them into their respective x and y variables. Then, the if statement compares x and y. 
# If the condition of x < y is met, the print statement is executed.
# If statements use bool or boolean values (true or false) to decide whether or not to execute. If the statement of x > y is true, the compiler will register it as true and execute the code.

### Control Flow, elif, and else
## Further revise your code as follows:

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")
## Notice how you are providing a series of if statements. First, the first if statement is evaluated. Then, the second if statement runs its evaluation. Finally, the last if statement runs its evaluation.
#  This flow of decisions is called “control flow.”
## Our code can be represented as follows:



### This program can be improved by not asking three consecutive questions. 
# After all, not all three questions can have an outcome of true! Revise your program as follows:

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
## Notice how the use of elif allows the program to make less decisions.
#  First, the if statement is evaluated. If this statement is found to be true, all the elif statements not be run at all. However, if the if statement is evaluated and found to be false, the first elif will be evaluated. If this is true, it will not run the final evaluation.

### OR statements
# or allows your program to decide between one or more alternatives.for example , we could further edit our code as follows:
x= int(input("What's x? "))
y= int(input("What's y? "))
if x<y or x>y:
    print("x is not equal to y")
else:
    print("x is equal to y")
# Notice how the or statement allows the program to decide between two alternatives. If either of the conditions is true, the program will run the code. If both conditions are false, the else statement will run.
# at this point our code is pretty graet , however ,could the design be further improved? we could further edit our code as foloows:
x= int(input("What's x? "))
y= int(input("What's y? "))
if x != y :
    print("x is not equal to y")
else:
    print("x is equal to y")
# Notice how the use of the != operator allows us to simplify our code. We can also use the == operator to simplify our code:
x= int(input("What's x? "))
y= int(input("What's y? "))
if x == y :
    print("x is equal to y")
else:
    print("x is not equal to y")
# Notice how the use of the == operator allows us to simplify our code. We can also use the != operator to simplify our code:

### AND statements
# similar to or, and can be used within conditional statements to allow your program to decide between one or more alternatives.
# for example, we could further edit our code as follows:
score = int(input("Score: "))
if score >= 90 and score <= 100:
    print("Grade: A")
elif score>=80 and score <90:
    print("Grade: B")
elif score>=70 and score <80:
    print("Grade: C")
elif score>=60 and score <70:
    print("Grade: D")
else:
    print("Grade: F")
# Notice how the and statement allows the program to decide between two alternatives. If both of the conditions are true, the program will run the code. If either condition is false, the else statement will run.
# at this point our code is pretty great, however, could the design be further improved? we could further edit our code as follows:
score = int(input("Score: "))
if 90<= score <=100:
    print("Grade: A")
elif 80<= score <90:
    print("Grade: B")
elif 70<= score <80:
    print("Grade: C")
elif 60<= score <70:
    print("Grade: D")
else:
    print("Grade: F")
# Notice how the use of the >= and <= operators allows us to simplify our code. We can also use the == operator to simplify our code:
score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
# Notice how the use of the >= operator allows us to simplify our code. We can also use the == operator to simplify our code:

### Modulo Operator
#In mathematics, parity refers to whether a number is either even or odd. 
# The modulo % operator in programming allows one to see if two numbers divide evenly or divide and have a remainder.
# For example, 4 % 2 would result in zero, because it evenly divides. However, 3 % 2 does not divide evenly and would result in a number other than zero!

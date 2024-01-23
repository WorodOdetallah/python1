x=int(input("What's x? "))
if x % 2 ==0:
    print("x is even")
else:
    print("x is odd")
# # Notice how the use of the % operator allows us to simplify our code. We can also use the == operator to simplify our code:
# Creating our own parity function 
def main():
    x=int(input("What's x? "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")
def is_even(n):
    if n % 2 ==0:
        return True
    else:
        return False
main()
# # Notice how we can use the return statement to simplify our code. We can also use the == operator to simplify our code:
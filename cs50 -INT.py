# int is not just a datatype but a fucntion too
# nesting int and input function
# we need to take the int function otherwise python treats user input as string by default
x=int(input("What's x?"))
y=int(input("What's y?"))
print(x+y)

# More compact way  (BUT NOT READABLE ENOUGH):
print(int(input("Enter x: "))+int(input("Enter y: ")))

#   FLOAT   
a=float(input("Enter a: "))
b=float(input("Enter b: "))

#   Round function :
#    round(number[, ndigits])
z=round(a+b,2)

#formatting
print(f"{z:,}")

n=round((a/b),2)
print(n)
print(f"{(a/b): .3f}")

# Using def and return keywords
def main():
    x1=int(input("What's x? "))
    print("x squared is equal to",square(x1))
def square(n):
    return n*n # or pow(n,2) or n**2
main
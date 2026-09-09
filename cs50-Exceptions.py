# Handling ValueError 
try:
    x=int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("This value is not an integer , so please enter an integer.")

# Avoiding NameError using else 
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

# Improvising , not giving up easily
while True:
    try:
        x=int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")
print(f"x is {x}")

# Handling exception while using fucntions
def main():
    x=get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            return(int(input("What's x?")))
        except ValueError:
            print("x is not an integer")
main()

# Using pass keyword 
def main():
    x=get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            return(int(input("What's x? ")))
        except ValueError:
            pass
main()

# Parameterizing an exception handler 
def main():
    x=get_int("What's x? ")
    print(f"x is {x}")
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()
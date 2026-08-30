x=int(input("What's x? "))
y=int(input("What's y?"))
if x<y:
    print("x is less than y")
elif x>y:
    print("y is less than x")
else:
    print("x and y are equal")

# or

if x<y or x>y:
    print("x and y are not equal")
else:
    print("x and y are equal")

# !
if x!=y :
    print("x is not equal to y")
else:
    print("x is equal to y")

# and

score=int(input("Score:"))
if score>=90 and score<=100:
    print("Grade: A")
# another way to write the conditions succinctly:
elif 80<=score<90:
    print("Grade: B")
# another way to write it succinctly :
elif score>=70:
    print("Grade: C")
elif score>=60:
    print("Grade: D")
else:
    print("Grade: F")

# Modulo Operator 

num=int(input("What's num? "))
if(num%2==0):
    print("This number is even...")
else:
    print("This number is odd...")

def main():
    x=int(input("What's num? "))
    if is_even(x):
        print("This number is even...")
    else:
        print("This number is odd...")
def is_even(n):
      return (n%2==0)
     #bool - True/False
    
main()

# match

name=input("What's your name? ")
match name:
     case "Harry"|"Hermione"|"Ron":
          print("Gryffindor")
     case "Draco":
           print("Slytherin")
     case _:
          print("Who?")    

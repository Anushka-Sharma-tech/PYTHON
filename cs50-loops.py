# while
i=1
while i<=3:
    print("meow")
    i+=1

# for 
for i in [0,1,2,3,4,5]:
    print("Meow")
for i in range(3):
    print(i)

# using underscore as a variable
for _ in range(2):
    print(_)

while True:
    n=int(input("What's n? "))
    if n>0:
        break

for _ in range(n):
    print("Meow")

def main():
    number=get_number()
    meow(number)
def meow(n):
    for _ in range(n):
        print("meow")
def get_number():
    while True:
     n=int(input("Enter a number "))
     if n>0:
         return n
main()

# Loops in LISTS

students=["Harry","Hermione","Ron"]
for student in students:
    print(student)
# Another Way
for i in range(len(students)):
    print(i+1,students[i])
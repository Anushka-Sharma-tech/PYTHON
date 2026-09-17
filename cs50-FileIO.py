# Using "with" to automate closing and we can use "a" instead of "w" in open function if we want to append instead of overwriting the existing file 

with open("Name.txt","w") as file:
    for _ in range (3):
        name=input("What's your name?")
        file.write(f"{name}\n")

# Reading an existing file

with open("Name.txt") as file:
    lines=file.readlines()
for line in lines:
    print("hello,",line.rstrip())

# Reading the file but printing in a sorted order 

with open("Name.txt") as file:
    lines=file.readlines()
for line in sorted(lines):
    print("hello,",line.rstrip())

# Sorting in reverse order 

with open("Name.txt") as file:
    lines=file.readlines()
for line in sorted(lines,reverse=True):
    print("hello,",line.rstrip())
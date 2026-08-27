#   String Functions
name=input("What's your name?")
print(name)

#   Remove whitespace from str
name=name.strip()
print(name)

#   Capitalize User's Input - It only capitalizes the very first letter
name= name.capitalize()
print(name)

#   title function - Capitalizes the first letter of each word
name= name.title()
print(name)

#   Chaining these functions
name=name.strip().title()

name1=input("What's your name?").strip().title()
print(name1)

#   Split User's name into first name and last name
first,last=name.split(" ")
print(f"hello,{first}")
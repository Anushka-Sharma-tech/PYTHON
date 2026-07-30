#BASIC PRINT FUNCTION
name=input("What is your name? ")
# print ("Hello ,",name )
'''
Official Documentation : Print Function
print(*objects, sep=' ', end='\n',file=sys.stdout,flush=false)
'''
print("How are you ",name," ?",sep="")
print("You look fine",end=" ")
print(name)

# Technique of escaping - Using backslash as an escape character
print("Hello, \"friend\".")
# format string- a special way to tell the function to format our string
print(f"Hello, {name}")

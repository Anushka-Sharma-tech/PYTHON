# To print a vertical line of blocks using abstraction ( creating functions to hide all the details):
# to print : #
             #
             #

def main():
    print_blocks(3)

def print_blocks(height):
    print("#\n"*height)
main()

# To print horizontal coins :
#        ????

def mainn():
    print_coins(4)
def print_coins(width):
    print("?"*width)
mainn()

# To print a square : ###
                      ###
                      ###
def mainnn():
    print_square(3)
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#",end="")
        print()
mainnn()
print("\n")

# Now by using mulltiplication
def main1():
    print_square(3)
def print_square(size):
    for i in range(size):
        print("#"*size)
main1()

# Now by using 3 functions
def main2():
    print_square(3)
def print_square(size):
    for i in range(size):
        print_row(size)
def print_row(size):
    print("#"*size)
main2()
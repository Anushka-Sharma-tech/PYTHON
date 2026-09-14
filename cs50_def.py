# def - define
def hello(to):
    print("hello,",to)
# To set a default value of the argument
def hellow(to="World"):
    return f"Hello, {to}"

# def-main
def main():
    name=input("what's your name? ")
    hello1(name)
    hellow1()

def hello1(to):
    print("Hello ",to)
def hellow1(to="World"):
    print("Hello,",to)




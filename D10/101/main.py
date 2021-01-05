def add(n1, n2):
    return n1 + n2

def subtact(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtact,
    "x": multiply,
    "/": divide
}

num1 = int(input("What is the first number"))
num2 = int(input("what is the second number"))

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

num1 = int(input("What is the first number")) #choosing first number

for symbol in operations:
    print(symbol)
operation_symbol = input("pick an operation from the line above: ") #choosing which operation

num2 = int(input("what is the second number")) #choosing 2nd number

calculation_function = operations[operation_symbol] #getting what user put in for operation and executing 
answer = calculation_function(num1,num2) #using operation executed with two numbers used 

print(f"{num1} {operation_symbol} {num2} = {answer}") #printing
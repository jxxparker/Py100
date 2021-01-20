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
first_answer = calculation_function(num1,num2) #using operation executed with two numbers used 

print(f"{num1} {operation_symbol} {num2} = {first_answer}") #printing

operation_symbol = input("pick another operation ") #choosing which operation
num3 = int(input("whats 3rd number"))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(first_answer,num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")


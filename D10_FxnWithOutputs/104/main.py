from art import logo

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
def calculator():
    print(logo)
    num1 = float(input("What is the first number ")) #choosing first number

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("pick an operation ") #choosing which operation
        num2 = float(input("what is the next number ")) #choosing 2nd number
        
        calculation_function = operations[operation_symbol] #getting what user put in for operation executing
        answer = calculation_function(num1,num2) #using operation executed with two numbers used 

        print(f"{num1} {operation_symbol} {num2} = {answer}") #printing

        if input(f"type 'y' to continue calculate with {answer}, or type 'n to start a new calculation") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()

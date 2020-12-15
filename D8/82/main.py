#Write your code below this line 👇
def prime_checker(number):
    if number == 2:
        print("its a prime number")
    if number == 3:
        print("it's a prime number")
    if number == 5:
        print("it's a prime number")
    if number % 2 == 0:
        print("not a prime number")
    if number % 3 == 0:
        print("not a prime number")
    if number % 5 == 0:
        print("not a prime number")
    
n = int(input("Check this number: "))
prime_checker(number=n)




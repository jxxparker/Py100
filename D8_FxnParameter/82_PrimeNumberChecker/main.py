def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0: #if this is able to dviide any number and get 0, its not a prime
            is_prime = False

    if is_prime:
        print("It's a prime number")
    else:
        print("Its not a prime number")
            
n = int(input("Check this number: "))
prime_checker(number=n)


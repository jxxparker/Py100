print("welcome to the rollercoaster!")
height = int(input("what is your height in cm?"))

if height > 120:
    print("Taller than 120, you are good")
    age = int(input("What is your age?"))
    if age < 12:
        print("please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("not taller than 120, you can not")
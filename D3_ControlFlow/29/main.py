print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("please pay $7")
    else:
        print("Please pay $12")
else :
    print("you can't ride the rollercoaster")

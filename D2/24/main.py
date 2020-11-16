totalBill = int(input("What was the total bill"))
whatPercentage = int(input("what percentage tip would you like to give? 10,12, or 15"))
howManyPeople = int(input("How many people to split the bill?"))

billWithPercentage = (totalBill) * ((whatPercentage/100) + 1)
print(billWithPercentage)
finalBill = round((billWithPercentage / howManyPeople) , 2)
print(f"Each person should pay ${finalBill}")
currentAge = input("how old are you?") #asking the age

til90 = (90 - int(currentAge)) #finding out how many years left depending on age
daysLeft = (til90 * 365) 
weeksLeft = (til90 * 52)
monthsLeft = (til90 * 12)

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")


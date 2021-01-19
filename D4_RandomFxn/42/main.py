import random

names_of_everybody = input("Give me everybodys names")
names = names_of_everybody.split(", ")
print(names)

num_items = len(names)
print(num_items)
random_choice = random.randint(0,  num_items - 1) #between 0 and 3
person_paying = names[random_choice]

print(person_paying + " is going to pay. thanks!")
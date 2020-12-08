import random
# import my_module

random.seed(321) #initiliazer


random_integer = random.randint(1,10)
print(random_integer)

# print(my_module.pi)

random_float = random.random() * 5 #always generate 0-1
print(random_float)

love_score = random.randint(1,100)
print(f"your love score is {love_score}")
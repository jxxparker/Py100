#for loop with range
# for number in range(1, 11): #prints 1-10
#     print(number)

# for number in range(1, 11, 3): #prints 1, 4, 10 
#     print(number)

total = 0
for number in range(1, 101):
    total += number #adds every number from 1 - 100
print(total)
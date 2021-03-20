row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ") #lets say i put 32

horizontal = int(position[0]) #horizintal becomes 3, since position[0] = 3
print(horizontal) 
verticle = int(position[1]) #same logic as horizintal but with verticle
print(verticle) 

selected_row = map[verticle - 1] #have to subtract 1 since for programming reasons 0,1,2
selected_row[horizontal - 1] = "X" 

print(f"{row1}\n{row2}\n{row3}")






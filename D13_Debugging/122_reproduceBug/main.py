# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) #range is from 0 to 5, for random number
print(dice_num)
print(dice_imgs[dice_num])

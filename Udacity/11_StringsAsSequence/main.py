#sequences

#the first category of collections we examine are sequences - sized, iterable ordered containers of data.
#we'll see the similiarties and differences between three sequence types - list, tuple, and str

#three sequence types
#list
#tuple
#str

# s = "SCHOOLED"
# print(s[-4:])
# print(s[1::2])
# print(s[1] + s[3] + s[5] + s[7])
# print(s[::2])
# print(s[1] + s[3] + s[-3] + s[-1])
# print(s[::5])

# s1 = "Udacity"
# print(s1[0:2]) #Ud
# print(s1[4:7]) #ity
# print(s1[1:5]) #daci

# print(s[1:5:2]) #dc
# print(s[4::-2]) #iaU #if you omit reversing
# print(s[::-1]) #yticadU

# sa = "Hello World"
# print(sa[1])

# print(sa[-2])

# print(sa[-4:])
# print(sa[::-1])
# print(sa[::-4])

s2 = "ham cheese bacon eggs"
ingredients = s2.split()
print(ingredients)
print(ingredients[::2])
ingredients[1:-1] = ["spinach"]
print(ingredients)

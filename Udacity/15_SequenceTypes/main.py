# #In the # Slicing section, fill out the code with the correct slice values to get the proper outputs.

# hello = 'Hello, world!'
# a = hello[0].upper()
# print(a)

# b = hello[-2]
# print(b)

# c = hello[1:5]
# print(c)

# d = hello[7:12]
# print(d)

# e = hello[::2]
# print(e)

# f = hello[::-1]
# print(f)

#In the # Manipulating Strings section, write the make_palindrome function to convert a string into a palindrome whose prefix is the given string. Can you find the shortest possible palindrome?

def make_palindrome(s):
    return s + s[::-1] 
    
print(make_palindrome("hello world"))

#In the # Manipulating Lists and Tuples section, write the add_layer function to add a layer to a growing representation of Pascal's triangle.

def add_layer(triangle):
    last = triangle[-1]
    row = []
    for left, right in zip(last + (0,), (0,) + last):
        row.append(left + right)
    triangle.append(tuple(row))
    
    
pascals_triangle = [
    (1,),
    (1, 1),
    (1, 2, 1),
    (1, 3, 3, 1),
]

# Add a few layers, just to check.
for _ in range(5):
    add_layer(pascals_triangle)
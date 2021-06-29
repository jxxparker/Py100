#Sets
# - Unordered collection of distinct hashable elements

#  -- Efficiently checking if an element is contained in a collection
#  -- Eliminating duplicate entries from a collection
#  -- representing abstract sets, with access to mathemtcial operators such as intersection and union


# s = {1, 3, 4}
# set_from_list = set([1, 2, 3, 2, 3, 4, 3, 1, 2])

# s = set([1,4,9,16,25])
# print(set_from_list)

# basket = {"apple", "orange", "apple", "pear", "banana"}
# for fruit in basket:
#     print(fruit)


# a = set("mississippi")
# a.add('r')
# a.remove('m')
# a.discard('x')
# print(a)

a = set("abracadabra")
b = set("alacazam")
# print(a)

c = a - b
print(c)
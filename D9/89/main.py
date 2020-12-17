programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "Action of doing something over and over again"
}

# ["a",  "b", "c"]
# print(programming_dictionary["Function"])

# adding new items to dictionary
# programming_dictionary["Loop"] = "the action of doing something over and over again"
# print(programming_dictionary)

# #create an empty dictionary.
# empty_dictionary = {}

# #wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# #edit an iten in a dictionary
# programming_dictionary["Bug"] = "bug is bad for your computer"
# print(programming_dictionary)

#loop through a dictionary
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])
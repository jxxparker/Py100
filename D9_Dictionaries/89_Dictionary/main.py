programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    # "Loop": "The action of doing something over and over again",
    }

#retrievcing items from dictionary
# print(programming_dictionary["Bug"])

#adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
# print(programming_dictionary)


#create an empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your compputer"
# print(programming_dictionary)

#loop through a dictionary
for thing in programming_dictionary:
    print(thing) #bug, fxn, loop

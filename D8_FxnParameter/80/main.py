def greet():
    print("Hello")
    print("Howdo you do")
    print("Isn't the weather nice today")
#greet()

def greet_with_name(name):
    print(f"hello {name}")
    print(f"how doyou do {name}")

# greet_with_name("jihun")

#function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Location is {location}")

greet_with("james", "chicago")
greet_with(location="london", name="mike")

# namespaces(or symbol table) is an associative mapping from (variable) names to objects

x = 47320
y = "Hello"

# variable assignment
# -assigning from a variable does not copy an object
# - instead, it adds another reference to the same object 
# - python always h andles the creation (and destruction!) of new objects

x = "Hello there"

# >>> x = "Hello there"
# >>> print(x)
# Hello there
# >>> y = x
# >>> id(x)
# 140625993601328
# >>> x is y
# True
# >>> z = "Hello"
# >>> z += " there"
# >>> x is z
# False
# >>> id(z)
# 140626005727344
# >>> id(x)
# 140625993601328
# >>> locals()['x']
# 'Hello there'
# >>> locals()['z']
# 'Hello there'

# Recap
# everything is an object
#  - an object has a type and an identity
#  - an object is like suitcase
#  - use == to compare values and is compare identities

# a variable is a name associated to an object via a namespace
#  - variable assignment adds a new local reference to an object

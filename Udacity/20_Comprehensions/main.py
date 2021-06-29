squares = []

for x in range(10):
    squares.append(x ** 2) 

print(squares)

print([ x ** 2 for x in range(10) ])

print({x: x ** 2 for x in range(10) if x % 2 == 0} )


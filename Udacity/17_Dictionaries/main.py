#dictionary

#mutable map from hashtable keys to arbitrary values


# d = {"one": 1, "two": 2, "three": 3}

# print(d['one'])
# # print(d['five']) #error

# d['two'] = 22 #modify
# d['four'] = 4  # Add a new key
# print(d)


#-----------------------
temps = {'CA': [101, 115, 108], 'NY': [98, 102]}
print(temps)
print(temps.get('CA'))

ky_temps = temps.get('KY', [])
num_observations = len(ky_temps)
print(num_observations)
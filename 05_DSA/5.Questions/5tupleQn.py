coordinate = (10,20)
print(coordinate)
print(coordinate[0],coordinate[1])
# coordinate[0] = 50  it'wont work kyuki these are immutable
print()
print()

new_cood = list(coordinate)
new_cood[0] = 50 #after converting it to a list we can do changes
print(new_cood)
print(new_cood[0],new_cood[1])
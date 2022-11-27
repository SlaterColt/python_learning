my_tuple = (1, 'strings', 4.5, True)
print((my_tuple.count('strings')))

print(my_tuple.index(4.5))

for x in my_tuple:
    print(x)

    # tuples are immutable (cannot be changed)

# my_tuple[0] = 5 
# The line above will throw a TypeError
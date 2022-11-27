sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Water'}

my_d = {1: 'Test', 'Name': 'Jim'}

print((my_d[1]))
my_d[2] = 'Test 2'

my_d[1] = 'Not a test'
del my_d[1]
#print(my_d)

for key, value in my_d.items():
    print(str(key) + ' : ' + value)
list1 = [1, 2, 3, 4, 5]

list2 = ['A', 'B', 'C']

list3 = ['Hello', 1, True, 40.22]

#print(list1, sep=" ")

list1.append(6)

list1.extend([7, 8, 9])

print(list1, sep=" ")

del list1[2]

for x in list1:
    print('Value', x)

print(*list1)
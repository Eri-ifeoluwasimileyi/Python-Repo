list = [10, 20, 30, 40, 50]

print(list[2])
print()

list = ['red', 'green', 'blue']
list[2] = 'yellow'
print(list)
print()

list.append('purple')
print(list)
print()

list = [1, 2, 3, 4, 5]
list.remove(2)
print(list)
print()

list = ['Alice', 'Bob', 'Charlie']
new_list = []
for items in list:
	new_list.append(len(items))
print(new_list)
print()


list = [4, 1, 3, 9, 2]
list.sort()
print(list)
print()


list = [1, 3, 4, 10, 5, 6, 8]
def even(list):
	new_list = []
	for number in list:
		if number % 2 == 0:
			new_list.append(number)
	return new_list

print(even(list))
print()


list_A = [1, 2, 3]
list_B = [4, 5, 6]
list_A.extend(list_B)
print(list_A)
print()


name_list = ['lamb', 'kit', 'yam', 'kings', 'dogs', 'man']

another_list = []

for name in name_list:

	if len(name) > 3:

		another_list.append(name)
print(another_list)




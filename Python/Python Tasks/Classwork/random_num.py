import random


list = []

def random_number(list):

	for number in range(1, 11):
		digits = random.randint(1, 50)
		list.append(digits)

	return list


def length_of_number(list):
	list_length = 0
	for number in list:
		list_length += 1

	return list_length



def even_number(list):
	add = 0
	for index in range(0, 10, 2):
		add += list[index]
	return add

def odd_number(list):
	add = 0
	for index in range(1, 10, 2):
		add += list[index]
	return add

def multiply(list):
	product = 1
	for number in range(2, 10, 3):
		product *= list[number]
	return product


def average_of_number(list):
	add = 0
	count = 0
	for number in list:
		count += 1
		add += number
	average = add / count
	return average




print(random_number(list))
print(length_of_number(list))
print(even_number(list))
print(odd_number(list))
print(multiply(list))
print(average_of_number(list))
def maximum(value1, value2, value3):
	max_value = value1
	if value2 > max_value:
		max_value = value2
	elif value3 > max_value:
		max_value = value3
	return max_value



print(maximum('yellow', 'red', 'orange'))

print(maximum(12.4, 46.5, 9.7))

print(maximum(11, 36, 28))

print(maximum(6, -3, 13.5))



def minimum(value1, value2, value3):
	min_value = value1
	if value2 < min_value:
		min_value = value2
	elif value3 < min_value:
		min_value = value3
	return min_value



print(minimum('yellow', 'red', 'orange'))

print(minimum(12.4, 46.5, 9.7))

print(minimum(11, 36, 28))

print(minimum(6, -3, 13.5))
cart = ['banana', 33, 'juice', 2.5, ['fish', 'palm oil'], True]
print(cart[0].upper())
print(cart[4][1])
print(len(cart))



scores = [50, 34, 45, 50, 25]

print("we have", len(scores), "scores")
print(scores[2])
print(scores[0:3:2]) #slicing

for score in scores:
	print(score)

for index in range(len(scores)):
	print(index)

enumerate(scores)
print(scores)

for value in enumerate(scores):
	print(value)

for tomi, value in enumerate(cart):
	print(tomi, ":", value)

print(dict(enumerate(cart)))

cart[4].insert(0, 6)
print(cart)


scores.extend([37, 67, 87, 65])
print(scores)

scores.append(99)
scores.pop(1)
print(scores)


print()
if 'banana' in cart:
	print("LOL") 

if 'apple' not in cart:
	print("LOOOOL") 


new_list = cart + scores
print(new_list)

print()

new_list = cart + scores
print(scores [-8])





























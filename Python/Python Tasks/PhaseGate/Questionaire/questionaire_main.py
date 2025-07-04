import random
import questionaire
from questionaire import *

questions = {0: first, 1: second, 2: third, 3: fourth, 4: fifth, 5: sixth, 6: seventh, 7: eighth, 8: ninth, 9: tenth}

random.shuffle(questions)

quest_count = 0
valid_answer = 0
invalid_answer = 0
score = 0

while quest_count < 10:

	user_choice = int(input('Pick a question from(1-10): '))

	if(user_choice < 1 or user_choice > 10):
		print('invalid number')
		continue

	user_choice = user_choice - 1

	if any(user_choice == index for index in questions):

		answer = questions[user_choice]
		answer(True)

		if answer:
			quest_count += 1
			valid_answer += 1
			score += 1

		else:
			quest_count += 1
			invalid_answer += 1

		questions.pop(user_choice)

	else:
		print('question already answered. choose another question.')
		continue


	
print("All done")
print(f'You got {valid_answer}, You failed {invalid_answer}.')
print(f'Your score is: {score}')

	



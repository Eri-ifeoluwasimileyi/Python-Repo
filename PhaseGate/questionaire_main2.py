import random
import questionaire
from questionaire import *

question = [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth]

random.shuffle(question)

asked_questions = []
quest_count = 0
valid_answer = 0
invalid_answer = 0
score = 0

while quest_count < 10:

	user_input = input('Pick a question number from (1-10): ')

	if not user_input.isdigit():

		print('Invalid input. Please enter a number between 1 and 10.')
		continue

	user_choice = int(user_input)

	if user_choice < 1 or user_choice > 10:
		print('Invalid number. Please choose between 1 and 10.')
		continue

	index = user_choice - 1

	if index in asked_questions:
		print('You have already answered this question. Choose another one.')
		continue

	asked_questions.append(index)

	question_function = question[index]

	result = question_function(True)

	if result:
		valid_answer += 1
		score += 1
	else:
		print("Max attempts reached.")
		invalid_answer += 1

	quest_count += 1


print("All done!")
print(f"You got {valid_answer} correct answer(s) and {invalid_answer} incorrect answer(s).")
print(f"Your total score is: {score} out of 10")

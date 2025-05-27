def add_a_task(list, task):

	list.append(task)

	return "added"


def view_all_tasks(list):

	for index, task in enumerate(list, 1):
		
		print(f"{index} {task}")

def mark_complete(list):

	for index, task in enumerate(list, 1):
	
		print(f"{index} {task}")

		if view == 1:
			print [X]

		else: view == 0
		print(f"{index} {task}")

def delete_task(list):

	for index, task in enumerate(list, 1):
	
		print(f"{index} {task}")
	
		if del == 1:
			task.pop(0)
		else: view == 0
		print(f"{index} {task}")

			
		

	







list = []


while True:

	print("""
	
	1. Add a task 
	
	2. View all tasks

	3. Mark a task as complete

	4. Delete a task

	5. Exit
		""")

	user_pick = str(input('Enter your choice: '))
	print()

	
	match(user_pick):

		case '1':

			task = input('Add a task: ')
			print(add_a_task(list, task))
		
		case '2':
	
			view_all_tasks(list)

		case '3':
			view_all_tasks(list)
			view = input('Pick 1 to tick: ')
			mark_complete(list)		

		case '4':
			del = int(input('Enter 1 to delete: '))
			delete_task(list)
			view_all_tasks(list)

		case '5': break




	

from to_do_list import *
list = []


while True:

	print("""
	1. Add a task 
	
	2. View all tasks

	3. Mark a task as complete

	4. Delete a task

	5. Exit
		""")

	choice = str(input('Enter your choice: '))
	print()

	
	match choice:

		case '1':

			task = input('Add a task: ')
			print(add_a_task(list, task))
		
		case '2':
	
			view_all_tasks(list)

		case '3':
			view_all_tasks(list)
			print()
			view = str(input('Pick a number to tick it off: '))
			print(mark_complete(list, view))

		case '4':
			view_all_tasks(list)
			print()
			delete = str(input('Enter a number to delete: '))
			print(delete_task(list, delete))
			

		case '5': 
			print("You did well today") 
			break


		case _: print("invalid input, try again")
			

def add_a_task(list, task):

	list.append(task)
	return "task added"


def view_all_tasks(list):

	for index, task in enumerate(list, 1):
		
		print(f"{index} {task}")

def mark_complete(list, pick):

	if not pick.isdigit():
		return "invalid input"

	pick = int(pick)

	for index, task in enumerate(list, 1):
		if pick == index:
			list[index - 1] += " : [X]"
			return "marked"


def delete_task(list, delete):

	if not delete.isdigit():
		return "invalid input"

	delete = int(delete)

	for index, task in enumerate(list, 1):
		if delete == index:
			list.pop(index - 1)
			return "deleted successfuly"
	








	
"""
App module
"""
__author__ = "Ram Basnet"

import project
import task

def menu():
	options = """
			Enter one of the options [1...6]:
			1: Reset Database
			2: Create Project
			3: Create Task
			4: Update Project
			5: Update Task
			6: Exit
			"""
	print(options)
	print('>>>: ', end='')
	option = int(input())
	return option

def main():
	while True:
		op = menu()
		if op == 6:
			exit()
		elif op == 1:
			yn = input("Are you sure? [y/n]: ").lower()
			if yn == 'y' or yn == 'yes':
				task.drop_table()
				project.drop_table()
				project.create_table()
				task.create_table()
		elif op == 2:
			name = input("Enter project name: ")
			st_date = input("When will the proect begin?: ")
			end_date = input("Enter end date: ")
			pr = (name, st_date, end_date)
			project.insert_table(pr)
		elif op == 3:
			create_new_task()

def show_projects():
	sql = f"SELECT * from {project._TABLE_NAME};"
	headers, rows = project.select_project(sql)
	for header in headers:
		print(header[0], end=' ')
	print()
	for row in rows:
		print(*row)

def create_new_task():
	show_projects()
	proj_id = int(input("Select a project id: "))
	#(name, priority, status_id, project_id, begin_date, end_date)
	name = input("Enter Task name: ")
	priority = int(input("Enter Task Priority [1-5]: "))
	status_id = int(input("Enter a status id [1-5]: "))
	begin_date = input("Enter begin date: ")
	end_date = input("Enter end date: ")
	new_task = (name, priority, status_id, proj_id, begin_date, end_date)
	task.insert_task(new_task)

if __name__ == "__main__":
	main()

"""
App module
"""
__author__ = "Ram Basnet"

import project
import task
import os

def menu():
	options = """
			Enter one of the options:
			1: Reset Database
			2: Create Project
			3: Create Task
			4: Update Project
			5: Update Task
			6: Show All Tasks
			7: Delete Task
			8: Show Project Tasks
			10: Exit
			"""
	print(options)
	print('>>>: ', end='')
	option = int(input())
	return option

def main():
	while True:
		op = menu()
		if op == 10:
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
		elif op == 5:
			update_task()
		elif op == 6:
			show_all_tasks()
		elif op == 7:
			delete_task()
		elif op == 8:
			show_project_tasks()

def show_project_tasks():
	show_projects()
	pr_id = int(input('Enter Project ID: '))
	sql = f'''
				SELECT id, name, priority, status_id, begin_date, end_date 
				FROM {task._TABLE_NAME} 
				WHERE project_id=?
				ORDER BY priority DESC
			'''
	title = f'Showing All Tasks For Project ID {pr_id}'
	print(f'{title:^94}')
	header = ['ID', 'Name', 'Priority', 'Project ID', 'Status ID', 'Begin Date', 'End Date']
	format = '{:^10}{:<30}{:^12}{:^12}{:<15}{:<15}'
	print(format.format(*header))
	print('='*94)
	_, rows = task.select_tasks(sql, (pr_id, ))
	#print(rows)
	for row in rows:
		print(format.format(*row))
	print('-'*94)
	input('Enter to continue...')

def update_task():
	os.system('clear')
	show_all_tasks()
	task_id = int(input('Enter Task ID to Update: '))
	priority = int(input("Enter Task Priority [1-5]: "))
	rows = task.select_task(f'select begin_date, end_date from {task._TABLE_NAME} where id= {task_id}')
	begin_date = rows[0][0]
	end_date = rows[0][1]
	data = (priority, begin_date, end_date, task_id)
	task.update_task(data)
	print('Task updated successfully...')
	input('Enter to continue...')
	show_all_tasks()

def delete_task():
	show_all_tasks()
	task_id = int(input('Enter Task ID to Delete: '))
	task.delete_task((task_id, ))
	show_all_tasks()

def show_all_tasks():
	os.system('clear')
	sql = f'''
				SELECT id, name, priority, project_id, status_id, begin_date, end_date 
				FROM {task._TABLE_NAME} 
				ORDER BY priority DESC
			'''
	headers, rows = task.select_tasks(sql)
	#for h in headers:
	print(f'{"Displaying All the Tasks":^106}', end='\n\n')
	print(f'{headers[0][0]:^10}', end='')
	print(f'{headers[1][0]:<30}', end='')
	print(f'{headers[2][0]:^12}', end='')
	print(f'{headers[3][0]:^12}', end='')
	print(f'{headers[4][0]:^12}', end='')
	print(f'{headers[5][0]:<15}', end='')
	print(f'{headers[6][0]:<15}')
	print('='*106)
	for row in rows:
		print('{:^10}{:<30}{:^12}{:^12}{:^12}{:<15}{:<15}'.format(*row))
	print('-'*106)
	input('Enter to continue...')

def show_projects():
	os.system('clear')
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
	begin_date = input("Enter begin date (yyyy-mm-dd): ")
	end_date = input("Enter end date (e.g.: 2022-12-31): ")
	new_task = (name, priority, status_id, proj_id, begin_date, end_date)
	task.insert_task(new_task)

if __name__ == "__main__":
	main()

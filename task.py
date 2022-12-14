"""
functions related to task table
"""
import db
import settings
import project

_TABLE_NAME = 'task'

def create_table():
	conn = db.create_connection(settings.DB_NAME)
	sql = f"""
					-- tasks table
					CREATE TABLE IF NOT EXISTS {_TABLE_NAME} (
						id integer PRIMARY KEY,
						name text NOT NULL,
						priority integer,
						project_id integer NOT NULL,
						status_id integer NOT NULL,
						begin_date text NOT NULL,
						end_date text NOT NULL,
						FOREIGN KEY (project_id) REFERENCES {project._TABLE_NAME} (id)
					);
					"""
	with conn:
		success = db.create_table(conn, sql)
		if success:
			print('Tasks table created successfully!')
		else:
			print("Tasks table couldn't be created!")

def insert_task(task:tuple):
  sql = f"""
          INSERT INTO {_TABLE_NAME}(name, priority, status_id, project_id, begin_date, end_date)
          VALUES(?,?,?,?,?,?);
        """
  # tasks
  
  conn = db.create_connection(settings.DB_NAME)
  with conn:
    cur = conn.cursor()
    cur.execute(sql, task)

def update_task(task:tuple):
	sql = f"""
				UPDATE {_TABLE_NAME} 
				SET priority = ?,
					begin_date = ?,
					end_date = ?
				WHERE id = ?
				"""
	conn = db.create_connection(settings.DB_NAME)
	with conn:
		cur = conn.cursor()
		cur.execute(sql, task)
	
def delete_task(task_id:tuple):
	sql = f"""
				DELETE FROM {_TABLE_NAME}
				WHERE id = ?
				"""
	conn = db.create_connection(settings.DB_NAME)
	with conn:
		cur = conn.cursor()
		cur.execute(sql, task_id)

def drop_table():
  conn = db.create_connection(settings.DB_NAME)
  sql = f"""
        DROP TABLE IF EXISTS {_TABLE_NAME};
        """
  with conn:
    cur = conn.cursor()
    cur.execute(sql)
    print(f'Table {_TABLE_NAME} dropped!')

def select_tasks(sql:str, para=None):
	conn = db.create_connection(settings.DB_NAME)
	rows = []
	headers = []
	if not para:
		para = ()
	with conn:
		cur = conn.cursor()
		cur.execute(sql, para)
		rows = cur.fetchall()
		#cur.execute(sql)
		headers = cur.description
	return headers, rows

def main():
	project_id = 1
	task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
	task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')
	insert_task(task_1)
	insert_task(task_2)

def test_update_task():
	task_id = 1
	begin_date = '2022-11-15'
	end_date = '2022-12-10'
	priority = 2
	task = (priority, begin_date, end_date, task_id)
	update_task(task)
	print("Task updated successfully!", task_id)

def test_delete_task():
	task_id = 1
	delete_task((task_id,))
	print(f'Task id: {task_id} deleted successfully!')

def select_task(sql:str):
	conn = db.create_connection(settings.DB_NAME)
	cur = conn.cursor()
	cur.execute(sql)
	rows = cur.fetchall()
	return rows

def test_select_task():
	sql = f"""
				SELECT * FROM {_TABLE_NAME};
				"""
	rows = select_task(sql)
	for row in rows:
		print(row)
	print('=======')
	sql = f"""
				SELECT * FROM {_TABLE_NAME}
				WHERE id = 2;
				"""
	rows = select_task(sql)
	for row in rows:
		print(row)

if __name__ == "__main__":
	#create_table()
	#main()
	#test_update_task()
	#test_delete_task()
	test_select_task()


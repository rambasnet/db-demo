"""
functions related to task table
"""
import db
import settings
import project

__TABLE_NAME = 'task'

def create_table():
  conn = db.create_connection(settings.DB_NAME)
  sql = f"""
          -- tasks table
          CREATE TABLE IF NOT EXISTS {__TABLE_NAME} (
            id integer PRIMARY KEY,
            name text NOT NULL,
            priority integer,
            project_id integer NOT NULL,
            status_id integer NOT NULL,
            begin_date text NOT NULL,
            end_date text NOT NULL,
            FOREIGN KEY (project_id) REFERENCES {project.__TABLE_NAME} (id)
          );
          """
    
  with conn:
    success = db.create_table(conn, sql)
    if success:
      print('Tasks table created successfully!')
    else:
      print("Tasks table couldn't be created!")

def insert_table():
  sql = f"""
          INSERT INTO {__TABLE_NAME}(name, priority, status_id, project_id, begin_date, end_date)
          VALUES(?,?,?,?,?,?)
        """
  # tasks
  project_id = 1
  task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
  task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')
  conn = db.create_connection(settings.DB_NAME)
  with conn:
    cur = conn.cursor()
    cur.execute(sql, task_1)
    cur.execute(sql, task_2)

if __name__ == "__main__":
  create_table()
  insert_table()

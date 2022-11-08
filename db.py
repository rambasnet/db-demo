__author__ = "Ram Basnet"
__date__ = "Nov 8, 2022"

"""
DB module 
- contains utility functions to work with sqlite db
"""
import sqlite3
import settings

# create_connection function
def create_connection(db_file: str):
  """
  function to connect to a sqlite db with given file db_file
  db_file: database file name
  return: None or conn
  """
  conn = None
  try:
    conn = sqlite3.connect(db_file)
    print('Connection successful...')
  except Exception as ex:
    print('Error: ', ex, db_file)
  return conn

def create_table(conn, sql:str) -> bool:
  """
  conn: sqlite connnection object
  sql: create table sql string
  return: True if table created successfully, False otherwise
  """
  try:
    cursor = conn.cursor()
    cursor.execute(sql)
    return True
  except Exception as ex:
    print('Error:', ex, sql)
    return False

def create_table_projects():
  conn = create_connection(settings.DB_NAME)
  with conn:
    sql = """
          CREATE TABLE IF NOT EXISTS projects (
            id integer primary key,
            name text NOT NULL,
            begin_date text,
            end_date text
          );
          """
    success = create_table(conn, sql)
    if success:
      print('Project table created successfully!')
    else:
      print('Project table could not be created!')
  
def create_table_tasks():
  conn = create_connection(settings.DB_NAME)
  sql = """
          -- tasks table
          CREATE TABLE IF NOT EXISTS tasks (
            id integer PRIMARY KEY,
            name text NOT NULL,
            priority integer,
            project_id integer NOT NULL,
            status_id integer NOT NULL,
            begin_date text NOT NULL,
            end_date text NOT NULL,
            FOREIGN KEY (project_id) REFERENCES projects (id)
          );
          """
    
  with conn:
    success = create_table(conn, sql)
    if success:
      print('Tasks table created successfully!')
    else:
      print("Tasks table couldn't be created!")
    
def test():
  conn = create_connection(settings.DB_NAME)
  with conn:
    sql = """
          CREATE TABLE IF NOT EXISTS projects (
            id integer primary key,
            name text NOT NULL,
            begin_date text,
            end_date text
          );
          """
    success = create_table(conn, sql)
    if success:
      print('Project table created successfully!')
    else:
      print('Project table could not be created!')

    sql = """
          -- tasks table
          CREATE TABLE IF NOT EXISTS tasks (
            id integer PRIMARY KEY,
            name text NOT NULL,
            priority integer,
            project_id integer NOT NULL,
            status_id integer NOT NULL,
            begin_date text NOT NULL,
            end_date text NOT NULL,
            FOREIGN KEY (project_id) REFERENCES projects (id)
          );
          """
    success = create_table(conn, sql)
    if success:
      print('Tasks table created successfully!')
    else:
      print("Tasks table couldn't be created!")

if __name__ == "__main__":
  test()
  create_table_projects()
  create_table_tasks()

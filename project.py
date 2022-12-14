"""
functions related to project table
"""
import db
import settings

_TABLE_NAME = "project"

def create_table():
  conn = db.create_connection(settings.DB_NAME)
  with conn:
    sql = """
          CREATE TABLE IF NOT EXISTS %s (
            id integer primary key,
            name text NOT NULL,
            begin_date text,
            end_date text
          );
          """%(_TABLE_NAME)

    success = db.create_table(conn, sql)
    if success:
      print('Project table created successfully!')
    else:
      print('Project table could not be created!')

def insert_table(project:tuple):
  sql = f"""
        INSERT INTO {_TABLE_NAME}(name, begin_date, end_date) VALUES 
        (?, ?, ?);
        """
  conn = db.create_connection(settings.DB_NAME)
  projectid = None
  with conn:
    try:
      cursor = conn.cursor()
      cursor.execute(sql, project)
      conn.commit()
      projectid = cursor.lastrowid
      print('Project inserted successfully...')
    except Exception as ex:
      print("Error: ", ex, sql, project)

  return projectid

def drop_table():
  conn = db.create_connection(settings.DB_NAME)
  sql = f"""
        DROP TABLE IF EXISTS {_TABLE_NAME};
        """
  with conn:
    cur = conn.cursor()
    cur.execute(sql)
    print(f'Table {_TABLE_NAME} dropped!')

def main():
  create_table()
  project = ("Final Project", "2022-11-10", "2022-12-10")
  pid = insert_table(project)
  print('project id: ', pid)
  #drop_table()

def select_project(sql:str):
	conn = db.create_connection(settings.DB_NAME)
	rows = []
	headers = []
	with conn:
		cur = conn.cursor()
		cur.execute(sql)
		rows = cur.fetchall()
		#cur.execute(sql)
		headers = cur.description
	return headers, rows

if __name__ == "__main__":
  main()
  
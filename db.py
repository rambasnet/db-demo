import sqlite3

# create_connection function
def create_connection(db_file):
  """
  function to connect to a sqlite db with given file db_file
  db_file: database file name
  return: None
  """
  conn = None
  conn = sqlite3.connect(db_file)
  print('connection successful...')
  print(sqlite3.version)
  conn.close()

if __name__ == "__main__":
  create_connection('gradebook.db')

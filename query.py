import sqlite3
import re
import columns_range

def search(data):
  connection = sqlite3.connect('database/data.db')
  connection.create_function('regexp', 2, regexp)
  connection.row_factory = dict_factory
  cursor = connection.cursor()
  
  query = generate_query(data)
  res = cursor.execute(f"SELECT * from masterlist {query}")
  res = res.fetchall()
  connection.close()
  
  return res

def regexp(pattern, text):
  if type(text) == str:
    pattern = re.compile(pattern, flags=re.IGNORECASE)
    return bool(pattern.search(text.lower()))

  return False

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}
  
def generate_query(data):
  
  result = ''
  
  for (index, query) in enumerate(data.values()):
    column = query["column"]
    pattern = query["pattern"]
    operator = query["operator"]
    if column == "W:CF":
      range_query = columns_range.get(index, pattern)
      result += range_query
    else:
      if index == 0:
        result += f"WHERE [{column}] {operator} '{pattern}'"
      else:
        result += f" AND [{column}] {operator} '{pattern}'"
  
  return result
from flask import Flask, jsonify, request
import dataset
import os
import init_db

app = Flask(__name__)

return_template = [
  "Author(s)",
  "Title",
  "Research Topics",
  "Methodologies Used",
  "ID"
]

def search(kwargs):
  db = dataset.connect('sqlite:///database/data.db')
  table = db["masterlist"]
  query = table.find(**kwargs)
  res = []
  for item in query:
    temp = {}
    for key in return_template:
      temp[key] = item[key]
    res.append(temp)
    
  return res

# Define your API endpoints here
@app.route('/', methods=['POST'])
def home():
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
    data = request.json
    res = search(data)
    return jsonify({"count": len(res), "results": res})
  else:
    return 'Content-Type not supported!'

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 4000))
  init_db.create()
  app.run(debug=False, host='0.0.0.0', port=port)
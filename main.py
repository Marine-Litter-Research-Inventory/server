from flask import Flask, jsonify, request
import dataset
import os
import init_db
import query

app = Flask(__name__)

return_template = [
  "Author(s)",
  "Title",
  "Research Topics",
  "Methodologies Used",
  "ID"
]

# Define your API endpoints here
@app.route('/', methods=['POST'])
def home():
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
    data = request.json
    res = query.search(data)
    return jsonify({"count": len(res), "results": res})
  else:
    return 'Content-Type not supported!'
  
# @app.route('/')

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 4000))
  init_db.create()
  app.run(debug=True, host='0.0.0.0', port=port)
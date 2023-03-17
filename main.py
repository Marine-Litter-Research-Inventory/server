from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import os, time
from flask_apscheduler import APScheduler
import init_db
import query

return_template = [
  "Author(s)",
  "Title",
  "Research Topics",
  "Methodologies Used",
  "ID"
]

app = Flask(__name__)
CORS(app)

scheduler = APScheduler()
scheduler.init_app(app)

@scheduler.task("cron", id="db_regeneration", day="*")
def regenerateDB():
  init_db.create()

scheduler.start()


# Main endpoint
@app.route('/api', methods=['POST'])
@cross_origin()
def home():
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
    data = request.json
    res = query.search(data)
    return jsonify({"count": len(res), "results": res})
  else:
    return 'Content-Type not supported!'

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 8000))
  init_db.create()
  app.run(debug=True, host='0.0.0.0', port=port)
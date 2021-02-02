from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import json
from bson import ObjectId
from bson import json_util

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/ulta_db")

# Route to render data from Mongo
@app.route("/")
def home():
   ulta_data = []
   #Find data from the mongo database
   for data in mongo.db.ulta.find({}, {"_id":False}):
       ulta_data.append(data)
   #dumped_data = [json_util.dumps(data) for data in ulta_data]
   #cleaned_data = [json.loads(data) for data in dumped_data]

   #return jsonify(cleaned_data)
   return render_template("index.html", ulta_data = ulta_data)

if __name__ == "__main__":
    app.run(debug=True)
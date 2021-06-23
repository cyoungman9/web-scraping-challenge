from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)


app.config = "mongodb://localhost:27017"
mongo = PyMongo(app)

@app.route("/")
def home():

#   images = mongo.db.listings.find_one() 

    return render_template("index.html", images=images)



@app.route("/scrape")
def scraper():

    mars_data = scrape_mars.scrape()

#  mongo.db.listings.update({}, mars_data, upsert=True) 
    
  return redirect("/", code=302) 

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scraper

# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    # mars = mongo.db.mars_app.find_one()
    mars = mongo.db.collection.find_one()
    print(mars)
    # Return template and data
    return render_template("index.html", mars=mars)



# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    print("something")
    # Run the scrape function
    mars_data = mars_scraper.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

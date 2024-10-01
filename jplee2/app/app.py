import os
from flask import Flask, render_template, redirect, request, jsonify
from modelHelper import ModelHelper

#################################################
# Flask Setup
#################################################

os.chdir(os.path.dirname(os.path.realpath(__file__)))
app = Flask(__name__)
modelHelper = ModelHelper()

#################################################
# Flask Routes
#################################################

# HTML ROUTES
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict")
def predict():
    return render_template("index.html")

@app.route("/dashboard1")
def dashboard1():
    return render_template("tableau_1.html")

@app.route("/dashboard2")
def dashboard2():
    return render_template("tableau_2.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/work_cited")
def work_cited():
    return render_template("workcited.html")

@app.route("/makePredictions", methods=["POST"])
def make_predictions():
    content = request.json["data"]
    print(content)

    # parse
    sex = int(content["sex"])
    age = float(content["age"])
    height = float(content["height"])
    weight = int(content["weight"])
    name_of_country = int(content["country"])
    year = content["year"]
    season = content["season"]
    sport = content["sport"]

    preds = modelHelper.makePredictions(sex, age, height, weight, name_of_country, year, season, sport)
    return(jsonify({"ok": True, "prediction": str(preds)}))

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

# Run the App
if __name__ == '__main__':
    app.run(debug=True)
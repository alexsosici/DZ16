from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def index():
    some_text = "PORUKA OD HENDLERA."
    current_year = datetime.datetime.now().year
    cities = ["Rovinj", "Poreč", "Pula", "Novigrad"]
    return render_template("index.html", some_text=some_text, current_year=current_year, cities=cities)

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("fakebook.html")
@app.route("/portfolio/boogle")
def boogle():
    return render_template("boogle.html")

if __name__ == '__main__':
    app.run()
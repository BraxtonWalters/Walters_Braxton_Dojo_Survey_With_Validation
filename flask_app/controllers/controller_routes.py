from flask_app import app
from flask import render_template, redirect, request, session

# landing page
@app.route("/")
def landing():
    locations = ["Chicago", "Seattle", "Online", "Burbank", "Bellevue"]
    languages = ["HTML", "CSS", "JavaScript", "Python", "C#"] 
    return render_template("index.html", locations = locations, languages=languages)
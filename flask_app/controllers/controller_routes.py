from flask import app, render_template, redirect, request, session

# landing page
@app.route("/")
def landing():
    return render_template("index.html")
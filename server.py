from flask_app import app
from flask import render_template, redirect, request, session
# import controllers 
from flask_app.controllers import controller_routes
from flask_app.controllers import controller_dojo




if __name__ == "__main__":
    app.run(debug=True)
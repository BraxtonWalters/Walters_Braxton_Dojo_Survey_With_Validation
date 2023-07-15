from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_dojo import Dojo


@app.route("/info/create", methods=["POST"])
def info_create():
    if not Dojo.validator(request.form):
        return redirect("/")
    data = {**request.form}
    dojo_id = Dojo.create(data)
    return redirect(f"/info/display/{dojo_id}")

# @@@@@@@@@@@@@@@@@@@@@@@@ AAAAAAAAAAPPPPPPPPPPPPPPPPP RRRRRRRROUTTTEEEEEEE
@app.route("/info/display/<int:id>")
def info_display(id):
    info = Dojo.get_dojo(id)
    return render_template("submitted.html", info=info)
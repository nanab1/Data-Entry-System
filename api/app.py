from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from .models import Security, VehicleInfo
# from flask_migrate import Migrate
import os
username = "postgres"
password = "kojo1234"
database = "rtsms_db"


app = Flask(__name__)
app.secret_key = "secret-key"
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{username}:{password}@localhost:5432/{database}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config.from_mapping()

db = SQLAlchemy(app)

    
# db.init_app(app)
# migrate = Migrate(app, db)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    return render_template("view.html", values = User.query.all())

@app.route("/login" ,methods=['GET',"POST"])
def login():
    if request.method == "POST":
        username=request.form['username']
        sec_idNo=request.form['id']
        location=request.form['location']

        print(username, location, id)
        found_user = Security.query.filter_by(name=username).first()
        if found_user:
            if sec_idNo == found_user.sec_idNo:
                session['location'] = found_user.location
                session['username'] = found_user.username
                session['sec_idNo'] = found_user.sec_idNo

                flash("Login Succesful!")
                return redirect(url_for("record"))
            else:
                flash("Incorrect username or ID", "error")
        else:
            flash(f"There is no username,{username} in the record. Please see the admin to sign up ", 'error')
    else:
        if "username" in session:
            flash("You have already Logged in!")
            return redirect(url_for("record"))
    return render_template("login.html")

@app.route("/record", methods=["POST", "GET"])
def record():
    if "username" in session:
        location = session['location']
        
        if request.method == "POST":
            vehicleNumber = request.form["vehicleNumber"]
            driverName = request.form["driverName"]
            routeTo = request.form["routeTo"]
            post = session["location"]

            vehicle_record = VehicleInfo(vehicleNumber=vehicleNumber, driverName=driverName, routeTo=routeTo, post=post).first()
            db.session.add(vehicle_record)
            db.session.commit()
            flash("Record has been saved")
        return render_template("user.html", location=location)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    flash("You have been logged out", "info")
    session.pop("username", None)
    session.pop("sec_idNo", None)
    session.pop("location", None)
    return redirect(url_for("login"))












# @app.route("/vehicle_info" ,methods=["POST"])
# def vehicle_info():
#     if request.method == "POST":
#         lv_no=request.form['lv_no']
#         driver_name=request.form['driver_name']
#         route_to=request.form['route_to']

#         print(lv_no, driver_name, route_to)
#         redirect("monitoring_form.html")
#     return render_template("login.html")
# @app.route("/<name>")
# def user(name):
#     return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)








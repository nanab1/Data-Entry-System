from flask import Flask, render_template, request, redirect, url_for, session, flash

from api.models import db, Security, VehicleInfo
# from flask_migrate import Migrate
import os


app = Flask(__name__)
app.secret_key = "secret-key"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config.from_mapping()



    
db.init_app(app)
# migrate = Migrate(app, db)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    return render_template("view.html", values = Security.query.all())


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        fullname = request.form['name']
        sec_idNo = request.form['sec_idNo']
        temp = fullname.split()
        length = len(temp)
        username = f"{temp[0][0]}{temp[-1]}"

        new_user = Security(name=fullname, sec_idNo=sec_idNo, username=username)
        db.session.add(new_user)
        db.session.commit()
        flash(f"Your username is {username}")
        redirect(url_for("login"))
    return render_template("signUp.html")
    
@app.route("/login" ,methods=['GET',"POST"])
def login():
    if request.method == "POST":
        username=request.form['username']
        sec_idNo=request.form['sec_idNo']
        location=request.form['location']

        print(username, location, id)
        found_user = Security.query.filter_by(username=username).first()
        if found_user:
            if sec_idNo == found_user.sec_idNo:
                session['location'] = location
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
            driverName = request.form["driver_name"]
            routeTo = request.form["route_to"]
            post = session["location"]

            vehicle_record = VehicleInfo(vehicle_number=vehicleNumber, driver_name=driverName, route_to=routeTo, post=post)
            db.session.add(vehicle_record)
            db.session.commit()
            flash("Record has been saved")
        return render_template("monitoring_form.html", location=location)
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








from flask import Flask, render_template, request, redirect

import os

def create_app():
    #Create and configure the app
    app = Flask(__name__)
    app.config.from_mapping()



    @app.route("/" ,methods=['GET',"POST"])
    def login():
        if request.method == "POST":
            username=request.form['username']
            location=request.form['location']

            print(username, location)
        return render_template("login.html")

    return app




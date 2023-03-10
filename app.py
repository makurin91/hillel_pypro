import json
from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'my_secret_key'
FILE = "memory/data.json"


def save_credentials(email, password):
    with open(FILE, "r") as infile:
        data = json.load(infile)
        if email in data:
            print("Email already exist")
            return False
        else:
            data[email] = password
            with open(FILE, "w") as outfile:
                json.dump(data, outfile)
                print("Email and password is saved")
                return True


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if password != confirm_password:
            flash('Check your passwords')
            save_credentials(email, password)
            return render_template('registration.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    if request.method == 'POST':
        password = request.form.get('password')
        if password != 'string':
            return redirect(url_for('registration'), code=302)
    return render_template('login.html')

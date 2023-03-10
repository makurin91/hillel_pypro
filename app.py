import json
from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'my_secret_key'
FILE = "memory_file/data.json"
REGISTRATION_PAGE = "registration.html"
LOGIN_PAGE = "login.html"
STYLE = "style.css"


def save_credentials(email, password):
    with open(FILE, "r") as infile:
        data = json.load(infile)
        if email in data:
            return False
        data[email] = password
        with open(FILE, "w") as outfile:
            json.dump(data, outfile)
            return True


def check_password(email, password):
    with open(FILE, "r") as infile:
        data = json.load(infile)
        return email in data and data[email] == password


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    url_for('static', filename=STYLE)
    if request.method == 'GET':
        return render_template(REGISTRATION_PAGE)
    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if password != confirm_password:
            flash('Password and confirm password does not match')
            return render_template(REGISTRATION_PAGE)
        else:
            result = save_credentials(email, password)
            if result is False:
                flash('This user already exist')
                return redirect(url_for('login'), code=302)
            else:
                flash('You are successfully registered')
                return redirect(url_for('login'), code=302)


@app.route("/login", methods=['GET', 'POST'])
def login():
    url_for('static', filename=STYLE)
    if request.method == 'GET':
        return render_template(LOGIN_PAGE)
    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        result = check_password(email, password)
        if result is True:
            flash('You are logged in')
            return render_template(LOGIN_PAGE)
        else:
            flash('Your email or password is incorrect')
            return render_template(LOGIN_PAGE)

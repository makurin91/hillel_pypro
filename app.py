import os
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/registration", methods=['GET', 'POST'])
def registration(*args, **kwargs):
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    print(email)
    print(password)
    print(confirm_password)
    return render_template('registration.html')


@app.route("/login", methods=['GET', 'POST'])
def login(*args, **kwargs):
    email = request.form.get('email')
    password = request.form.get('password')
    if request.method == 'POST':
        password = request.form.get('password')
        if password != 'string':
            return redirect(url_for('registration'), code=302)
    return render_template('login.html')

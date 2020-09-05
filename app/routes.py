from flask import render_template, flash, redirect, url_for, send_file
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

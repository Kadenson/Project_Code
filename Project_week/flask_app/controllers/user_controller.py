from flask_app import app
from flask import render_template, redirect, request, session, flash


@app.route('/')
def main_page():
    return render_template('index.html')
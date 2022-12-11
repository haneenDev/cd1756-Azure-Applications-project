"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect, request, session, url_for
from werkzeug.urls import url_parse



@app.route('/')
@app.route('/home')
@login_required
def home():
    return "Flask API get endpoint running.."


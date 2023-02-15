# app.py
from flask import Flask, render_template, request
from registration import registration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a very long string'
from flask import render_template, request, redirect

from flask_app import app
# import the class from dojo.py
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    if Dojo.is_valid(request.form):
        Dojo.save(request.form)
        return redirect('/result')
    return redirect('/')

@app.route('/result')
def result():
    print(request.form)
    return render_template("result.html", dojo = Dojo.get_one())
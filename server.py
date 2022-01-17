from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key="just@test"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    print(request.form)
    return render_template("result.html",name_on_template=session['name'], location_on_template=session['location'],
    language_on_template=session['language'], comments_on_template=session['comments'])

if __name__=="__main__":
    app.run(debug=True)
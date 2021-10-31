from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "skittles"

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/results')
def result():
    return render_template('results.html')

@app.route('/process', methods = ["POST"])
def form_process():
    session['full_name'] = request.form['full_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    print(session['location'])
    return redirect('/results')


if __name__ == "__main__":
    app.run(debug=True)
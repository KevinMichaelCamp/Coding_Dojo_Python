from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA_Z0-9._-]+\.[a-zA-z]+$')
app = Flask(__name__)
app.secret_key = 'MySecretKey'

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    print(request.form)
    if len(request.form['name']) < 1:
        flash("Name cannot be empty")
    else:
        flash(f"Success! Your name is {request.form['name']}.")
    if len(request.form['email']) < 1:
        flash("Email cannot be empty")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address")
    else:
        flash("Valid Email Address")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

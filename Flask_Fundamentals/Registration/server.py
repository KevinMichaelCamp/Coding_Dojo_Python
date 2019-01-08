from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA_Z0-9._-]+\.[a-zA-z]+$')
NAME_REGEX = re.compile(r'[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'MySecretKey'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/validate', methods=['POST'])
def validate():

    # first_name
    if len(request.form['first_name']) < 1:
        flash("First Name cannot be blank")
    elif not NAME_REGEX.match(request.form['first_name']):
        flash("First Name must contain only letters")
    else:
        session['first_name'] = request.form['first_name']

    # last_name
    if len(request.form['last_name']) < 1:
        flash("Last Name cannot be blank")
    elif not NAME_REGEX.match(request.form['last_name']):
        flash("Last Name must contain only letters")
    else:
        session['last_name'] = request.form['last_name']

    # email
    if len(request.form['email']) < 1:
        flash("Email cannot be blank")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email address")
    else:
        session['email'] = request.form['email']

    # password
    if len(request.form['password']) < 9:
        flash("Password must be at least 9 characters")
    else:
        session['password'] = request.form['password']

    # password confirmation
    if request.form['confirmation'] != request.form['password']:
        flash("Password confirmation does not match password")
    else:
        pass

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return render_template('success.html')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

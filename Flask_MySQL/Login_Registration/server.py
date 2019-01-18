from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA_Z0-9._-]+\.[a-zA-z]+$')
NAME_REGEX = re.compile(r'[a-zA-Z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'MySecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods = ['POST'])
def validate():

    if len(request.form['first_name']) < 2:
        flash("First name must contain at least 2 letters", 'first_name')
    elif not NAME_REGEX.match(request.form['first_name']):
        flash("First name muse contain letters only", 'first_name')
    else:
        session['first_name'] = request.form['first_name']

    if len(request.form['last_name']) < 2:
        flash("Last name must contain at least 2 letters", 'last_name')
    elif not NAME_REGEX.match(request.form['last_name']):
        flash("Last name muse contain letters only", 'last_name')
    else:
        session['last_name'] = request.form['last_name']

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email format", 'email')
    else:
        session['email'] = request.form['email']

    if len(request.form['password']) < 8:
        flash("Password must have at least 8 characters", 'password')
    elif request.form['password'] != request.form['confirm']:
        flash("Password does not match password confirmation", 'confirmation')
    else:
        session['password'] = request.form['password']

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return redirect('/register')

@app.route('/register')
def register():
    mysql = connectToMySQL('login_register')
    query = ("INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(),NOW())")
    hashed_pw = bcrypt.generate_password_hash(session['password'])
    data = {
        'first_name': session['first_name'],
        'last_name': session['last_name'],
        'email': session['email'],
        'password': hashed_pw
    }
    new_user_id = mysql.query_db(query, data)
    print(new_user_id)

    return redirect('/success')


@app.route('/login', methods = ['POST'])
def login():
    mysql = connectToMySQL('login_register')
    email = request.form['email']
    query = "SELECT id, first_name, password FROM users WHERE users.email = %(email)s"
    data = {
        'email': email,
    }

    loggedIn_user = mysql.query_db(query, data)

    if loggedIn_user:
        if bcrypt.check_password_hash(loggedIn_user[0]['password'], request.form['password']):
            session['id'] = loggedIn_user[0]['id']
            session['first_name'] = loggedIn_user[0]['first_name']
            return redirect('/success')
        else:
            flash("Login failed: invalid email/password", 'login')
            return redirect('/')
    else:
        flash("Login failed: invalid email/password", 'login')
        return redirect('/')


@app.route('/success')
def success():
    if 'email' in session:
        flash(session['first_name'] + ", You have successfully registered.")
    mysql = connectToMySQL('login_register')
    all_users = mysql.query_db("SELECT id, first_name, last_name, email FROM users;")

    return render_template('success.html', all_users = all_users, first_name = session['first_name'])

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out", 'logout')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

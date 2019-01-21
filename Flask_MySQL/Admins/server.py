from flask import Flask, flash, render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "MySecretkey"
EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'[a-zA-Z]+$')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/validate', methods=['POST'])
def validate():

    mysql = connectToMySQL('flask_admin')
    query = "SELECT email FROM users WHERE email = %(email)s;"
    data = {
        'email': request.form['email']
    }
    duplicate_email = mysql.query_db(query, data)

    if len(request.form['first_name']) < 2:
        flash("First name must be at least 2 letters long", 'first_name')
    elif not NAME_REGEX.match(request.form['first_name']):
        flash("First name must be only letters", 'first_name')
    else:
        session['first_name'] = request.form['first_name']

    if len(request.form['last_name']) < 2:
        flash("Last name must be at least 2 letters long", 'last_name')
    elif not NAME_REGEX.match(request.form['last_name']):
        flash("Last name must be only letters", 'last_name')
    else:
        session['last_name'] = request.form['last_name']

    if len(request.form['email']) < 1:
        flash("Please enter email address", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email format", 'email')
    elif duplicate_email:
        flash("Email already exists in database", 'email')
    else:
        session['email'] = request.form['email']

    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters long", 'password')
    elif request.form['password'] != request.form['confirmation']:
        flash("Password confirmation does not match password", 'confirmation')
    else:
        session['password'] = bcrypt.generate_password_hash(
            request.form['password'])

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return redirect('/register')


@app.route('/login', methods=['POST'])
def login():
    mysql = connectToMySQL('flask_admin')
    query = "SELECT id, user_level, first_name, last_name, email, password FROM users WHERE email = %(email)s;"
    data = {
        'email': request.form['email']
    }
    loggedIn_user = mysql.query_db(query, data)

    if loggedIn_user:
        if bcrypt.check_password_hash(loggedIn_user[0]['password'], request.form['password']):
            session['id'] = loggedIn_user[0]['id']
            session['first_name'] = loggedIn_user[0]['first_name']
            if loggedIn_user[0]['user_level'] == 9:
                return redirect('/admin')
            else:
                return redirect('/users')
        else:
            flash("Invalid email/password", 'login')
            return redirect('/')
    else:
        flash("Invalid email/password", 'login')
        return redirect('/')


@app.route('/register')
def register():

    mysql = connectToMySQL('flask_admin')
    query = "INSERT INTO users (user_level, first_name, last_name, email, password, created_at, updated_at) VALUES(%(user_level)s, %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())"
    data = {
        'user_level': 1,
        'first_name': session['first_name'],
        'last_name': session['last_name'],
        'email': session['email'],
        'password': session['password']
    }
    new_user_id = mysql.query_db(query, data)

    return redirect('/users')


@app.route('/users')

def users():
    return render_template('users.html')


@app.route('/admin')
def admin():
    mysql = connectToMySQL('flask_admin')
    query = "SELECT id, user_level, first_name, last_name, email FROM users;"
    all_users = mysql.query_db(query)

    return render_template('admin.html', all_users=all_users)


@app.route('/delete', methods=['POST'])
def delete():
    mysql = connectToMySQL('flask_admin')
    query = "DELETE FROM users WHERE id = %(id)s"
    data = {
        'id': request.form['id']
    }
    mysql.query_db(query, data)

    return redirect('/admin')


@app.route('/addAdmin', methods=['POST'])
def addAdmin():
    mysql = connectToMySQL('flask_admin')
    query = "UPDATE USERS SET user_level = %(user_level)s WHERE id = %(id)s;"
    data = {
        'user_level': 9,
        'id': request.form['addAdmin']
    }
    updated_user = mysql.query_db(query, data)

    return redirect('/admin')


@app.route('/removeAdmin', methods=['POST'])
def removeAdmin():
    mysql = connectToMySQL('flask_admin')
    query = "UPDATE USERS SET user_level = %(user_level)s WHERE id = %(id)s;"
    data = {
        'user_level': 1,
        'id': request.form['removeAdmin']
    }
    updated_user = mysql.query_db(query, data)

    return redirect('/admin')


@app.route('/logout')
def logout():
    session.clear()
    flash("You have logged off", 'logout')
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

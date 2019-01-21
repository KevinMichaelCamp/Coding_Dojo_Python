from Login_Reg import app
from flask import flash, request, session
from Login_Reg.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA_Z0-9._-]+\.[a-zA-z]+$')
NAME_REGEX = re.compile(r'[a-zA-Z]+$')
bcrypt = Bcrypt(app)
app.secret_key = 'MySecretkey'


class Validate():
    def index(self):
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
        return


class Register():
    def index(self):
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
        return new_user_id


class Login():
    def index(self):
        mysql = connectToMySQL('login_register')
        email = request.form['email']
        query = "SELECT id, first_name, password FROM users WHERE users.email = %(email)s"
        data = {
            'email': email,
        }

        loggedIn_user = mysql.query_db(query, data)
        return loggedIn_user


class Success():
    def index(self):
        if 'email' in session:
            flash(session['first_name'] +
                  ", You have successfully registered.")
        mysql = connectToMySQL('login_register')
        all_users = mysql.query_db(
            "SELECT id, first_name, last_name, email FROM users;")
        return all_users


class Logout():
    def index(self):
        session.clear()
        return

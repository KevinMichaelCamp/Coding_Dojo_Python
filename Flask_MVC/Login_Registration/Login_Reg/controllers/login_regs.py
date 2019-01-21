from Login_Reg import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from Login_Reg.models.login_reg import Validate, Register, Login, Success, Logout

bcrypt = Bcrypt(app)
validate = Validate()
register = Register()
login = Login()
success = Success()
logout = Logout()


class Indices():
    def index(self):
        return render_template('index.html')


class Validates():
    def index(self):
        validate.index()
        if '_flashes' in session.keys():
            return redirect('/')
        else:
            return redirect('/register')


class Registers():
    def index(self):
        new_user_id = register.index()
        return redirect('/success')


class Logins():
    def index(self):
        loggedIn_user = login.index()
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


class Successes():
    def index(self):
        all_users = success.index()
        return render_template('success.html', all_users=all_users, first_name=session['first_name'])


class Logouts():
    def index(self):
        logout.index()
        return redirect('/')

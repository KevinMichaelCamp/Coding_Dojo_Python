from flask import Flask, flash, render_template, redirect, request, session
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'MySecretkey'
EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'[a-zA-Z]+$')


@app.route('/')
def index():
    mysql = connectToMySQL('flask_users')
    query = "SELECT id, first_name, last_name, email, created_at FROM users"
    all_users = mysql.query_db(query)
    return render_template('index.html', all_users=all_users)


@app.route('/addUser')
def addUser():
    return render_template('newUser.html')


@app.route('/validate', methods=['POST'])
def validate():
    if len(request.form['first_name']) < 2:
        flash("First name must contain at least 2 letters", 'first_name')
    elif not NAME_REGEX.match(request.form['first_name']):
        flash("First name must only contain letters", 'first_name')
    else:
        session['first_name'] = request.form['first_name']

    if len(request.form['last_name']) < 2:
        flash("Last name must contain at least 2 letters", 'last_name')
    elif not NAME_REGEX.match(request.form['last_name']):
        flash("Last name must only contain letters", 'last_name')
    else:
        session['last_name'] = request.form['last_name']

    if len(request.form['email']) < 1:
        flash("Please enter email address", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email is in invalid format", 'email')
    else:
        session['email'] = request.form['email']

    if '_flashes' in session.keys():
        return redirect('/addUser')
    else:
        return redirect('/create')


@app.route('/create')
def create():
    mysql = connectToMySQL('flask_users')
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
    data = {
        'first_name': session['first_name'],
        'last_name': session['last_name'],
        'email': session['email'],
    }
    new_user_id = mysql.query_db(query, data)
    return redirect('/')


@app.route('/show/<id>')
def show(id):
    mysql = connectToMySQL('flask_users')
    query = "SELECT id, first_name, last_name, email, created_at, updated_at FROM users WHERE id = %(id)s;"
    data = {
        'id': id
    }
    user = mysql.query_db(query, data)
    return render_template('show.html', user=user)


@app.route('/edit/<id>')
def edit(id):
    session['id'] = id
    return render_template('edit.html', id=id)


@app.route('/update', methods=['POST'])
def update():

    id = session['id']

    if len(request.form['first_name']) < 2:
        flash("First name must contain at least 2 letters", 'first_name')
    elif not NAME_REGEX.match(request.form['first_name']):
        flash("First name must only contain letters", 'first_name')
    else:
        session['first_name'] = request.form['first_name']

    if len(request.form['last_name']) < 2:
        flash("Last name must contain at least 2 letters", 'last_name')
    elif not NAME_REGEX.match(request.form['last_name']):
        flash("Last name must only contain letters", 'last_name')
    else:
        session['last_name'] = request.form['last_name']

    if len(request.form['email']) < 1:
        flash("Please enter email address", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email is in invalid format", 'email')
    else:
        session['email'] = request.form['email']

    if '_flashes' in session.keys():
        return redirect('/edit/' + id)

    else:
        mysql = connectToMySQL('flask_users')
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        data = {
            'first_name': session['first_name'],
            'last_name': session['last_name'],
            'email': session['email'],
            'id': id
        }

        updated_user = mysql.query_db(query, data)
        return redirect('/')


@app.route('/delete/<id>')
def delete(id):
    mysql = connectToMySQL('flask_users')
    query = "DELETE FROM users WHERE id = %(id)s;"
    data = {
        'id': id
    }

    deleted_user = mysql.query_db(query, data)

    return redirect('/')


@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

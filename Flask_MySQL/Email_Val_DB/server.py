from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA_Z0-9._-]+\.[a-zA-z]+$')
app = Flask(__name__)
app.secret_key = 'MySecretKey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods = ['POST'])
def validate():
    mysql = connectToMySQL('emails')
    all_emails = mysql.query_db('SELECT * FROM emails')

    for i in all_emails:
        if i['email'] == request.form['email']:
            flash('Email already in database!')
            return redirect('/')

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email address is not valid!")

    else:
        mysql = connectToMySQL('emails')
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES(%(email)s, NOW(), NOW());"
        data = {'email': request.form['email']}
        new_email_id = mysql.query_db(query, data)
        session['email'] = request.form['email']

    if '_flashes' in session.keys():
        return redirect ('/')
    else:
        return redirect('/success')

@app.route('/delete', methods = ['POST'])
def delete():
    mysql = connectToMySQL('emails')
    query = "DELETE FROM emails WHERE email = %(email)s;"
    data = {'email': request.form['button']}
    mysql.query_db(query, data)
    return redirect('/success')

@app.route('/success')
def success():
    mysql = connectToMySQL('emails')
    all_emails = mysql.query_db("SELECT * FROM emails;")
    return render_template('success.html', all_emails = all_emails, curr_email = session['email'])

@app.route('/goback')
def goback():
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

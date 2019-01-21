from flask import request, session, flash
from mysqlconnection import connectToMySQL
from Email import app
import re

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA_Z0-9._-]+\.[a-zA-z]+$')
app.secret_key = 'MySecretKey'


class Validate():
    def index(self):
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

            return new_email_id


class Delete():
    def index(self):
        mysql = connectToMySQL('emails')
        query = "DELETE FROM emails WHERE email = %(email)s;"
        data = {'email': request.form['button']}
        mysql.query_db(query, data)
        return


class Success():
    def index(self):
        mysql = connectToMySQL('emails')
        all_emails = mysql.query_db("SELECT * FROM emails;")
        return all_emails

from flask import render_template, redirect, session
from Email import app
from Email.models.email import Validate, Delete, Success

validate = Validate()
delete = Delete()
success = Success()


class Indices:
    def index(self):
        return render_template('index.html')


class Validates:
    def index(self):
        validate.index()
        if '_flashes' in session.keys():
            return redirect('/')
        else:
            return redirect('/success')


class Deletes:
    def index(self):
        delete.index()
        return redirect('/success')


class Successes:
    def index(self):
        all_emails = success.index()
        return render_template('success.html', all_emails=all_emails, curr_email=session['email'])


class GoBacks:
    def index(self):
        return redirect('/')

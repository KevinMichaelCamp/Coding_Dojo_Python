from flask import render_template, redirect
from Email import app
from Email.controllers.emails import Indices, Validates, Deletes, Successes, GoBacks

indices = Indices()
validates = Validates()
deletes = Deletes()
successes = Successes()
gobacks = GoBacks()


@app.route('/')
def index():
    return indices.index()


@app.route('/validate', methods=['POST'])
def validate():
    return validates.index()


@app.route('/delete', methods=['POST'])
def delete():
    return deletes.index()


@app.route('/success')
def success():
    return successes.index()


@app.route('/goback')
def goback():
    return gobacks.index()

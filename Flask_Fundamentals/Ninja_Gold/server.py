from flask import Flask, render_template, redirect, request, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'MySecretKey'


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html', activities=session['activities'])


@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['location'] == 'farm':
        money = random.randrange(10, 21)
        message = "<p>You earned " + str(money) + " gold in the farm!</p>"
        session['activities'].append(message)
    elif request.form['location'] == 'cave':
        money = random.randrange(5, 11)
        message = "<p>You earned " + str(money) + " gold in the cave!</p>"
        session['activities'].append(message)
    elif request.form['location'] == 'house':
        money = random.randrange(2, 6)
        message = "<p>You earned " + str(money) + " gold in the house!</p>"
        session['activities'].append(message)
    else:
        money = random.randrange(-50, 51)
        message = "<p>You earned/lost " + \
            str(money) + " gold in the casino!</p>"
        session['activities'].append(message)

    session['gold'] = session['gold'] + money

    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

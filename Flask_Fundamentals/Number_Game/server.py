from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = 'MySecretKey'


@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randrange(1, 101)

    print("Number is " + str(session['number']))
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])

    if guess == session['number']:
        return redirect('/correct')
    elif guess < session['number']:
        return redirect('/low')
    else:
        return redirect('/high')


@app.route('/correct')
def correct():
    return render_template('correct.html')


@app.route('/low')
def low():
    return render_template('incorrect.html', result='Too Low!')


@app.route('/high')
def high():
    return render_template('incorrect.html', result='Too High!')


@app.route('/reset')
def reset():
    session.pop('number')
    return redirect('/')


if __name__ == ('__main__'):
    app.run(debug=True)

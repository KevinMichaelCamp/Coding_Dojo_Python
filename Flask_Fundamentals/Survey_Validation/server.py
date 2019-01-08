from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'MySecretKey'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users', methods=['POST'])
def create_user():
    print(request.form)

    location = request.form['location']
    language = request.form['language']

    if len(request.form['name']) < 1:
        flash("Name cannot be blank")
    else:
        name = request.form['name']

    if len(request.form['comment']) < 1:
        flash("Comments cannot be blank")
    elif len(request.form['comment']) > 120:
        flash("Comments must be less than 120 characters")
    else:
        comment = request.form['comment']


    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)

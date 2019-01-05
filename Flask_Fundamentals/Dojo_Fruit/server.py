from flask import Flask, render_template, redirect, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkout', methods=['POST'])
def checkout():

    print(request.form)

    dt = datetime.now()
    fulldate = dt.strftime('%B %d, %Y %I:%M:%S %p')

    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    orange = request.form['orange']
    banana = request.form['banana']
    name = request.form['name']
    id = request.form['id']

    fruit = (strawberry+raspberry+apple+orange+banana)
    return render_template('checkout.html', fulldate = fulldate)

if __name__=="__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print("Recieved POST data")
    print(request.form)
    print('Name', request.form['name'])
    print('Email', request.form['email'])
    name = request.form['name']
    email = request.form['email']
    return render_template('success.html')

if __name__=="__main__":
    app.run(debug=True)

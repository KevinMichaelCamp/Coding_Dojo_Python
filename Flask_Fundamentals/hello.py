from flask import Flask
app = Flask(__name__)

print(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/coding')
def coding():
    return "<h1>Coding Dojo</h1>"

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "hello " + name

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__=="__main__":
    app.run(debug=True)

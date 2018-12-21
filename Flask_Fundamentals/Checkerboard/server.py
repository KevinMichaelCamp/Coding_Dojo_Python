from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', x=int(8), y=int(8))


@app.route('/<x>/<y>')
def checkerboard(x, y):
    return render_template('index.html', x=int(x), y=int(y))
    pass


if __name__ == '__main__':
    app.run(debug=True)

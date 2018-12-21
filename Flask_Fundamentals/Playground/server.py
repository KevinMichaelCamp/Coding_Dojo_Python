from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('/index.html', num = int(3))

@app.route('/play/<num>')
def play_num(num):
    return render_template('/index.html', num = int(num), color = 'lightblue')

@app.route('/play/<num>/<color>')
def play_num_col(num,color):
    return render_template('/index.html', num = int(num), color = color)

if __name__ =='__main__':
    app.run(debug=True)

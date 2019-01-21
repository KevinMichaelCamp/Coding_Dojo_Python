from Login_Reg import app
from Login_Reg.controllers.login_regs import Indices, Validates, Registers, Logins, Successes, Logouts

indices = Indices()
validates = Validates()
registers = Registers()
logins = Logins()
successes = Successes()
logouts = Logouts()


@app.route('/')
def index():
    return indices.index()


@app.route('/validate', methods=['POST'])
def validate():
    return validates.index()


@app.route('/register')
def register():
    return registers.index()


@app.route('/login', methods=['POST'])
def login():
    return logins.index()


@app.route('/success')
def success():
    return successes.index()


@app.route('/logout')
def logout():
    return logouts.index()

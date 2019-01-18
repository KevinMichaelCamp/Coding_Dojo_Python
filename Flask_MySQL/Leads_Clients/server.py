from flask import Flask, render_template, redirect, request, session
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'MySecretKey'

@app.route('/')
def index():

    mysql = connectToMySQL('lead_gen_business')
    client_leads = mysql.query_db("SELECT clients.first_name, clients.last_name, COUNT(leads.id) AS 'num_leads' FROM clients JOIN sites ON clients.id = sites.clients_id JOIN leads ON sites.id = leads.sites_id GROUP BY clients.id ORDER BY num_leads DESC")
    session['date_leads'] = client_leads
    return render_template('index.html', client_leads = client_leads)

@app.route('/dates', methods = ['POST'])
def dates():
    mysql = connectToMySQL('lead_gen_business')
    query = ("SELECT clients.first_name, clients.last_name, COUNT(leads.id) AS 'num_leads' FROM clients JOIN sites ON clients.id = sites.clients_id JOIN leads ON sites.id = leads.sites_id WHERE leads.registered_datetime > %(start_date)s AND leads.registered_datetime < %(end_date)s GROUP BY clients.id ORDER BY num_leads DESC")
    data = {
        'start_date': request.form['start_date'],
        'end_date': request.form['end_date']
    }
    session['date_leads'] = mysql.query_db(query, data)
    return redirect('/repopulate')

@app.route('/repopulate')
def repopulate():
    return render_template('index.html', client_leads = session['date_leads'])

if __name__ == "__main__":
    app.run(debug=True)

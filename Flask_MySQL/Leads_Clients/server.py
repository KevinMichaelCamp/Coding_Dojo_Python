from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():

    mysql = connectToMySQL('lead_gen_business')
    client_leads = mysql.query_db("SELECT clients.first_name, clients.last_name, COUNT(leads.id) AS 'num_leads' FROM clients JOIN sites ON clients.id = sites.clients_id JOIN leads ON sites.id = leads.sites_id GROUP BY clients.id ORDER BY num_leads DESC")

    return render_template('index.html', client_leads = client_leads)


if __name__ == "__main__":
    app.run(debug=True)

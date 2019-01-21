from flask import redirect, render_template, request
from Friends.config.mysqlconnection import connectToMySQL

class Friends:
    def index(self):
        mysql = connectToMySQL('friendsdb')
        query = "SELECT * FROM friends"
        all_friends = mysql.query_db(query)
        return render_template('index.html', friends = all_friends)

class NewFriends:
    def create(self):
        mysql = connectToMySQL('friendsdb')
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'occupation': request.form['occupation']
        }
        new_friend_id = mysql.query_db(query, data)
        return redirect('/')

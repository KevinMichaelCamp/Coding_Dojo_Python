from Friends import app
from Friends.controllers.friends import Friends, NewFriends
friends = Friends()
new_friends = NewFriends()

@app.route('/')
def index():
    return friends.index()


@app.route('/create', methods=['POST'])
def create():
    return new_friends.create()

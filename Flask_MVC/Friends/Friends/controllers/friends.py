from flask import redirect, render_template
from Friends.models.friend import Friend, NewFriend
friend = Friend()
newfriend = NewFriend()

class Friends:
    def index(self):
        all_friends = friend.index()
        return render_template('index.html', friends = all_friends)

class NewFriends:
    def create(self):
        new_friend = newfriend.create()
        return redirect('/')

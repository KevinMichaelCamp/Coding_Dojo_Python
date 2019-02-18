from apps.user_login.models import *

#retrieve all users
User.objects.all()

#retrieve last user
User.objects.last()

# create a few records in users
User.objects.create(first_name='Kevin', last_name='Camp', email='kcamp4632@yahoo.com', age='39')

# retrive first user
User.objects.first()

# Know how to get the users sorted by their first name (order by first_name DESC)
User.objects.all().order_by('first_name')

# Get the record of the user whose id is 3 and UPDATE the person's last_name to something else. Know how to do this directly in the console using .get and .save.

u = User.objects.get(id=2)
u.last_name = 'Tate'
u.save

# Know how to delete a record of a user whose id is 4 (use something like User.objects.get(id=2).delete...).
User.objects.get(id=4).delete()
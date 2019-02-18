# Create 3 dojos
Dojo.objects.create(name='CodingDojo Silicon Valley', city='Mountain view', state='CA')

# Delete dojos
Dojo.objects.all().delete()

# Create 3 dojos
Dojo.objects.create(name='CodingDojo Silicon Valley', city='Mountain view', state='CA')

# Create ninjas
Ninja.objects.create(first_name='Kevin', last_name='Camp', dojo = Dojo.objects.first())

# Be able to retrieve all ninjas that belong to the first Dojo
Dojo.objects.first().ninjas.all()

# Be able to retrieve all ninjas that belong to the last Dojo
Dojo.objects.last().ninjas.all()

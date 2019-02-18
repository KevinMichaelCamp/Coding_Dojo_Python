# Create 5 books with the following names: C sharp, Java, Python, PHP, Ruby
Book.objects.create(name='C Sharp')

# Create 5 different authors: Mike, Speros, John, Jadee, Jay
Author.objects.create(first_name='Mike')

# Change book 1 name to C#
In [10]: b1 = Book.objects.first()

In [11]: b1.name = 'C#'

In [12]: b1.save()

# Change the first_name of the 5th author to Ketul
In [14]: a5 = Author.objects.get(id=5)

In [15]: a5.first_name='Ketul'

In [16]: a5.save()

# Assign the first author to the first 2 books
In [28]: b2 = Book.objects.get(id=2)
		a1 = Author.objects.first()
In [29]: b2.authors.add(a1)

# Assign the second author to the first 3 books
In [28]: b2 = Book.objects.get(id=2)
		a2 = Author.objects.get(id=2)
In [29]: b2.authors.add(a1)

#retrieve books
a3.books.all()
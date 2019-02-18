In [1]: from apps.likes_books.models import *

In [2]: Book.objects.create(name='Skinny Legs and All', desc='Tom Robbins book', uploader = u1)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-2-7c7f24cf9d02> in <module>
----> 1 Book.objects.create(name='Skinny Legs and All', desc='Tom Robbins book', uploader = u1)

NameError: name 'u1' is not defined

In [3]: u1 = User.objects.first()

In [4]: Book.objects.create(name='Skinny Legs and All', desc='Tom Robbins book', uploader = u1)
Out[4]: <Book object: Skinny Legs and All Tom Robbins book

In [5]: u2 = User.objects.get(id=2)

In [6]: Book.objects.create(name='Still Life with Woodpecker', desc='Tom Robbins book', uploader = u2)
Out[6]: <Book object: Still Life with Woodpecker Tom Robbins book

In [7]: Book.objects.create(name='Star Wars', desc='Star Wars', uploader = u2)
Out[7]: <Book object: Star Wars Star Wars

In [8]: u3 = User.objects.last()

In [9]: Book.objects.create(name='Empire Strikes Back', desc='Star Wars', uploader = u3)
Out[9]: <Book object: Empire Strikes Back Star Wars

In [10]: Book.objects.create(name='Return of the Jedi', desc='Star Wars', uploader = u3)
Out[10]: <Book object: Return of the Jedi Star Wars

In [11]: last_book = Book.objects.last()

In [12]: u1.liked_books
Out[12]: <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager at 0xa108c70>

In [13]: u1.liked_books.__dict__
Out[13]:
{'_constructor_args': ((<User object: Kevin Camp kcamp4632@yahoo.com,), {}),
 'creation_counter': 17,
 'model': apps.likes_books.models.Book,
 'name': None,
 '_db': None,
 '_hints': {},
 'instance': <User object: Kevin Camp kcamp4632@yahoo.com,
 'query_field_name': 'liked_users',
 'prefetch_cache_name': 'liked_books',
 'source_field_name': 'user',
 'target_field_name': 'book',
 'symmetrical': False,
 'through': apps.likes_books.models.Book_liked_users,
 'reverse': True,
 'source_field': <django.db.models.fields.related.ForeignKey: user>,
 'target_field': <django.db.models.fields.related.ForeignKey: book>,
 'core_filters': {'liked_users__id': 1},
 'pk_field_names': {'user': 'id'},
 'related_val': (1,)}

In [14]: u1.liked_books.values()
Out[14]: <QuerySet []>

In [15]: u1.uploaded_books.values()
Out[15]: <QuerySet [{'id': 1, 'name': 'A Confederacy of Dunces', 'desc': 'Book about a funny idiot', 'uploader_id': 1, 'created_at': datetime.datetime(2019, 2, 17, 23, 41, 21, 200815, tzinfo=<UTC>), 'updated_at': datetime.datetime(2019, 2, 17, 23, 41, 21, 200815, tzinfo=<UTC>)}, {'id': 2, 'name': 'Skinny Legs and All', 'desc': 'Tom Robbins book', 'uploader_id': 1, 'created_at': datetime.datetime(2019, 2, 17, 23, 43, 45, 524311, tzinfo=<UTC>), 'updated_at': datetime.datetime(2019, 2, 17, 23, 43, 45, 524311, tzinfo=<UTC>)}]>

In [16]: last_book.liked_users.add(u1)

In [17]: b1 = Book.objects.first()

In [18]: b1.liked_users.add(u1)

In [19]: b1.liked_users.add(u2)

In [20]: b3 = Book.objects.get(id=3)

In [21]: b3.liked_users.add(u2)

In [22]: Book.objects.all().liked_users.add(u3)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-22-c9b905dd0c0f> in <module>
----> 1 Book.objects.all().liked_users.add(u3)

AttributeError: 'QuerySet' object has no attribute 'liked_users'

In [23]: b1.liked_users.add(u3)

In [24]: b2 = Book.objects.get(id=2)

In [25]: b4 = Book.objects.get(id=4)

In [26]: b5 = Book.objects.get(id=5)

In [27]: b2.liked_users.add(u3)

In [28]: b3.liked_users.add(u3)

In [29]: b4.liked_users.add(u3)

In [30]: b5.liked_users.add(u3)

In [31]: last_book.liked_users.add(u3)

In [32]: b1.liked_users.values()
Out[32]: <QuerySet [{'id': 1, 'first_name': 'Kevin', 'last_name': 'Camp', 'email': 'kcamp4632@yahoo.com', 'created_at': datetime.datetime(2019, 2, 17, 23, 36, 54, 271004, tzinfo=<UTC>), 'updated_at': datetime.datetime(2019, 2, 17, 23, 36, 54, 271004, tzinfo=<UTC>)}, {'id': 2, 'first_name': 'Bob', 'last_name': 'Vila', 'email': 'bobvila@yahoo.com', 'created_at': datetime.datetime(2019, 2, 17, 23, 37, 18, 964379, tzinfo=<UTC>), 'updated_at': datetime.datetime(2019, 2, 17, 23, 37, 18, 964379, tzinfo=<UTC>)}, {'id': 3, 'first_name': 'Loren', 'last_name': 'Ashton', 'email': 'bassnectar@yahoo.com', 'created_at': datetime.datetime(2019, 2, 17, 23, 37, 41, 296960, tzinfo=<UTC>), 'updated_at': datetime.datetime(2019, 2, 17, 23, 37, 41, 296960, tzinfo=<UTC>)}]>

In [33]: b1.uploader.values()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-33-8b714b6a939e> in <module>
----> 1 b1.uploader.values()

AttributeError: 'User' object has no attribute 'values'

In [34]: b1.uploader
Out[34]: <User object: Kevin Camp kcamp4632@yahoo.com

In [35]: b2.liked_users.values()
Out[35]: <QuerySet [{'id': 3, 'first_name': 'Loren', 'last_name': 'Ashton', 'email': 'bassnectar@yahoo.com', 'created_at': datetime.datetime(2019, 2, 17, 23, 37, 41, 296960, tzinfo=<UTC>), 'updated_at': datetime.datetime(2019, 2, 17, 23, 37, 41, 296960, tzinfo=<UTC>)}]>

In [36]: b2.uploader
Out[36]: <User object: Kevin Camp kcamp4632@yahoo.com

# Generated by Django 2.1.5 on 2019-02-17 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0005_auto_20190217_1357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
    ]

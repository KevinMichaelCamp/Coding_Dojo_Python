# Generated by Django 2.1.5 on 2019-02-17 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0003_auto_20190217_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-29 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_published_date_alter_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
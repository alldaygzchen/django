# Generated by Django 3.1.5 on 2022-12-19 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]

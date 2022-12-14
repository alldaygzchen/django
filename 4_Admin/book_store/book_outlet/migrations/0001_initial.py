# Generated by Django 3.1.5 on 2022-12-21 13:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('author', models.CharField(blank=True, default='', max_length=100)),
                ('is_bestselling', models.BooleanField(default=False)),
                ('slug', models.SlugField(default='')),
            ],
        ),
    ]

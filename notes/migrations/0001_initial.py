# Generated by Django 4.1.2 on 2022-10-29 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('note', models.TextField()),
                ('created_date', models.DateTimeField()),
                ('updated_date', models.DateTimeField()),
                ('trash', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('deadline', models.DateTimeField()),
                ('category', models.CharField(choices=[('Grocery', 'Grocery'), ('Travel', 'Travel'), ('Sports', 'Sports'), ('Office', 'Office'), ('Food', 'Food'), ('Weekend Plan', 'Weekend Plan'), ('Other', 'Other')], default='other', max_length=100)),
            ],
        ),
    ]

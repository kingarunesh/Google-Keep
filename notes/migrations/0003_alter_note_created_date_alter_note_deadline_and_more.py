# Generated by Django 4.1.2 on 2022-10-29 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_note_created_date_alter_note_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='deadline',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
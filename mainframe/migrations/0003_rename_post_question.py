# Generated by Django 3.2.7 on 2021-10-09 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainframe', '0002_auto_20211009_0919'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Question',
        ),
    ]

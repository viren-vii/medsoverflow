# Generated by Django 3.2.7 on 2021-10-27 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainframe', '0021_delete_downvotea'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upvotea',
            name='by',
        ),
    ]

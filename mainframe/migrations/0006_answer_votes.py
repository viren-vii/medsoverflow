# Generated by Django 3.2.7 on 2021-10-09 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainframe', '0005_question_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]

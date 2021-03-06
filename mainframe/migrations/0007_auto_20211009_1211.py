# Generated by Django 3.2.7 on 2021-10-09 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainframe', '0006_answer_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answer',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.7 on 2021-10-13 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainframe', '0013_auto_20211010_0712'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpvoteQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainframe.user')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainframe.question')),
            ],
        ),
        migrations.CreateModel(
            name='UpvoteA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainframe.answer')),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainframe.user')),
            ],
        ),
        migrations.CreateModel(
            name='DownvoteQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainframe.user')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainframe.question')),
            ],
        ),
        migrations.CreateModel(
            name='DownvoteA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainframe.answer')),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainframe.user')),
            ],
        ),
    ]

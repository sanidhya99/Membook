# Generated by Django 4.1.7 on 2023-03-28 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='pic',
            field=models.CharField(default='https://iili.io/HN6dJmF.png', max_length=2000),
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-30 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_alter_friends_friend_alter_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='like',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
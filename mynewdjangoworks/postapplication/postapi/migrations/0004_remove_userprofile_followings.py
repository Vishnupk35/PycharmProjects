# Generated by Django 4.0.6 on 2022-09-11 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postapi', '0003_alter_posts_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='followings',
        ),
    ]

# Generated by Django 2.2 on 2020-04-12 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-20 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='header_image',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='blog',
            name='profile_pic',
            field=models.TextField(default='img/default.png'),
        ),
    ]

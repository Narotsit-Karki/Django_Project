# Generated by Django 4.1.1 on 2022-09-28 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_remove_blog_category_blog_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.AddField(
            model_name='post_categories',
            name='blogs',
            field=models.ManyToManyField(to='home.blog'),
        ),
    ]
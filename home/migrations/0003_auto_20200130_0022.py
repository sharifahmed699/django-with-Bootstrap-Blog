# Generated by Django 2.2.6 on 2020-01-29 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Title',
            new_name='title',
        ),
    ]

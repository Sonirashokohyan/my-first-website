# Generated by Django 4.2.4 on 2023-08-28 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='descpription',
            new_name='message',
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-13 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('side_app', '0003_alter_phonebool_about'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PhoneBool',
            new_name='PhoneBook',
        ),
    ]

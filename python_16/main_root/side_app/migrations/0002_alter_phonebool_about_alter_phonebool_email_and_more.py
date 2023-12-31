# Generated by Django 4.2.5 on 2023-09-13 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('side_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonebool',
            name='about',
            field=models.CharField(max_length=50, verbose_name='About'),
        ),
        migrations.AlterField(
            model_name='phonebool',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='phonebool',
            name='lastname',
            field=models.CharField(max_length=30, verbose_name='LastName'),
        ),
        migrations.AlterField(
            model_name='phonebool',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='phonebool',
            name='phone',
            field=models.CharField(max_length=18, verbose_name='Phone'),
        ),
    ]

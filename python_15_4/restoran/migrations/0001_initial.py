# Generated by Django 4.2.5 on 2023-09-25 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restoran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('spec', models.CharField(max_length=50, verbose_name='spec')),
                ('address', models.CharField(max_length=70, verbose_name='address')),
                ('web_site', models.CharField(max_length=70, verbose_name='website')),
                ('phone', models.CharField(max_length=50, verbose_name='phone')),
            ],
        ),
    ]

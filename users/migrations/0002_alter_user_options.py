# Generated by Django 4.2.13 on 2024-08-13 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]

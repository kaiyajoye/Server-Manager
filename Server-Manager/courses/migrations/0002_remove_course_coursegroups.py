# Generated by Django 2.2.5 on 2022-12-11 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='courseGroups',
        ),
    ]

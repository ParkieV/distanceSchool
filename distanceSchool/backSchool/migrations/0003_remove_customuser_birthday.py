# Generated by Django 3.0.5 on 2020-04-22 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backSchool', '0002_auto_20200422_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='birthday',
        ),
    ]
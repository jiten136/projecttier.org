# Generated by Django 2.1.8 on 2019-05-16 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_auto_20190516_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='category',
        ),
    ]

# Generated by Django 3.2 on 2021-07-12 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_auto_20210712_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='like',
        ),
    ]

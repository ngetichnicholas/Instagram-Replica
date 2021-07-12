# Generated by Django 3.2 on 2021-07-12 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_auto_20210712_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follows',
            name='followee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='photos.profile'),
        ),
        migrations.AlterField(
            model_name='follows',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='photos.profile'),
        ),
    ]

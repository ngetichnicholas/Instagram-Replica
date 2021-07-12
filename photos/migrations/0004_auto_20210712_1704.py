# Generated by Django 3.2 on 2021-07-12 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0003_auto_20210712_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
        migrations.AddField(
            model_name='follows',
            name='followee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='photos.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='follows',
            name='follower',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='following', to='photos.profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='photo_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='like',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photolikes', to='photos.image'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userlikes', to=settings.AUTH_USER_MODEL),
        ),
    ]

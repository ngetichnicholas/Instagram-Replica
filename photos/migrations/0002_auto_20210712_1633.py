# Generated by Django 3.2 on 2021-07-12 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='like',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like',
            name='photo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='imagelikes', to='photos.image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='userlikes', to='auth.user'),
            preserve_default=False,
        ),
    ]

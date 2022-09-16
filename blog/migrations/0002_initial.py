# Generated by Django 4.1 on 2022-09-15 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.photos'),
        ),
        migrations.AddField(
            model_name='comment',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

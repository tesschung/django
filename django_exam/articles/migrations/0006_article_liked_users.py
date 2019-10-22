# Generated by Django 2.2.6 on 2019-10-22 07:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0005_auto_20191022_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]

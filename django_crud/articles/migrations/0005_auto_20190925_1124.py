# Generated by Django 2.2.5 on 2019-09-25 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20190925_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='article',
            name='sub_content',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]

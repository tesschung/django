# Generated by Django 2.2.5 on 2019-09-25 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_comment_question_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_question',
            name='comment_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Question'),
        ),
    ]
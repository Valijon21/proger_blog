# Generated by Django 3.2 on 2022-04-11 10:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_new_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
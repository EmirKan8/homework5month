# Generated by Django 4.2.4 on 2023-08-26 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='price',
        ),
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
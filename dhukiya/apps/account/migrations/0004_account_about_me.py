# Generated by Django 3.1.6 on 2021-02-11 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210211_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='about_me',
            field=models.TextField(null=True),
        ),
    ]

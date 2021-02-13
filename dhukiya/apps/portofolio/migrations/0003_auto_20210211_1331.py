# Generated by Django 3.1.6 on 2021-02-11 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0002_portofolio_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='portofolio',
            name='client',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
    ]

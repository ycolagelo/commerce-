# Generated by Django 3.1.1 on 2020-11-13 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20201113_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name=''),
        ),
    ]

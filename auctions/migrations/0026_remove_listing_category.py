# Generated by Django 3.1.1 on 2020-11-26 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0025_auto_20201125_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='category',
        ),
    ]
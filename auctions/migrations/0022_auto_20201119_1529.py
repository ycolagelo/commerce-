# Generated by Django 3.1.1 on 2020-11-19 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_auto_20201117_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidding_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
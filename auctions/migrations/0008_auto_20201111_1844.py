# Generated by Django 3.1.1 on 2020-11-11 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20201110_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='item',
        ),
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.image'),
        ),
    ]

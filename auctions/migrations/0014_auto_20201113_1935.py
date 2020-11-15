# Generated by Django 3.1.1 on 2020-11-13 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20201112_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='name',
            field=models.CharField(default='name', max_length=64),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='img', null=True, upload_to='images/', verbose_name=''),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
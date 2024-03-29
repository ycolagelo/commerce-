# Generated by Django 3.1.1 on 2020-11-16 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auto_20201113_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='product',
            new_name='listing_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='item',
            new_name='listing_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auctions.listing')),
                ('user_id', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

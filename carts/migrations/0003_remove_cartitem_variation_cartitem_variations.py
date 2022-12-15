# Generated by Django 4.1.4 on 2022-12-15 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
        ('carts', '0002_cartitem_variation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='variation',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]

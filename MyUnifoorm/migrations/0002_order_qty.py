# Generated by Django 5.0.4 on 2024-06-24 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyUnifoorm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Qty',
            field=models.IntegerField(default=0),
        ),
    ]

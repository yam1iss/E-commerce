# Generated by Django 5.0.4 on 2024-06-23 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ProductID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('ProductName', models.TextField()),
                ('ProdImg', models.ImageField(default='null', upload_to='productpic')),
                ('Description', models.TextField()),
                ('Price', models.FloatField()),
                ('Brand', models.CharField(max_length=20)),
                ('Size', models.CharField(max_length=4)),
                ('Color', models.CharField(max_length=10)),
                ('Quantity', models.IntegerField()),
                ('Material', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('Email', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=12)),
                ('Name', models.TextField()),
                ('PhoneNumber', models.CharField(max_length=13)),
                ('Address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderID', models.AutoField(primary_key=True, serialize=False)),
                ('OrderDate', models.DateField()),
                ('OrderStatus', models.CharField(max_length=20)),
                ('TotalAmount', models.FloatField()),
                ('ProductID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyUnifoorm.product')),
                ('Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyUnifoorm.user')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('ReviewID', models.AutoField(primary_key=True, serialize=False)),
                ('Comment', models.TextField()),
                ('ReviewDate', models.DateField()),
                ('OrderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyUnifoorm.order')),
                ('Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyUnifoorm.user')),
            ],
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-08 08:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'carts',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('product_info', models.CharField(max_length=100, null=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('delivery_invoice', models.CharField(max_length=20, null=True)),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]

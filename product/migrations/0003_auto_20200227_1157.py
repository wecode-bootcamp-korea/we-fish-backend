# Generated by Django 3.0.3 on 2020-02-27 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200226_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='end_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='theme',
            name='start_at',
            field=models.DateField(null=True),
        ),
    ]
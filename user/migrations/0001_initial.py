# Generated by Django 3.0.3 on 2020-02-25 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=50)),
                ('date_of_birth', models.CharField(max_length=50)),
                ('postcode', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=300)),
                ('detailed_address', models.CharField(max_length=300)),
                ('mobile', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='user',
            name='agreement',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='detailed_address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='postcode',
            field=models.CharField(max_length=30),
        ),
    ]

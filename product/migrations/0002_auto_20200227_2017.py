# Generated by Django 3.0.3 on 2020-02-27 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200225_2212'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'sections',
            },
        ),
        migrations.RenameModel(
            old_name='ProductStock',
            new_name='Stock',
        ),
        migrations.RemoveField(
            model_name='date',
            name='day',
        ),
        migrations.RemoveField(
            model_name='date',
            name='expired',
        ),
        migrations.RemoveField(
            model_name='product',
            name='imgage',
        ),
        migrations.RemoveField(
            model_name='review',
            name='image',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='image_url',
            field=models.URLField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User'),
        ),
        migrations.AddField(
            model_name='theme',
            name='end_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='theme',
            name='image_url',
            field=models.URLField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='theme',
            name='start_at',
            field=models.DateField(null=True),
        ),
        migrations.AlterModelTable(
            name='review',
            table=None,
        ),
        migrations.AlterModelTable(
            name='stock',
            table='stocks',
        ),
        migrations.AlterModelTable(
            name='themeproduct',
            table='theme_products',
        ),
        migrations.AddField(
            model_name='theme',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Section'),
        ),
    ]

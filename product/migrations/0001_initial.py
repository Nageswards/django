# Generated by Django 4.2.1 on 2023-05-21 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Food_cat',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
                ('item_price', models.IntegerField()),
                ('image_Food', models.ImageField(upload_to='product/')),
                ('food_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.food_type')),
            ],
            options={
                'db_table': 'Image_Food',
            },
        ),
    ]

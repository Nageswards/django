# Generated by Django 4.2.1 on 2023-05-22 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Goods_cat',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Goods_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
                ('item_price', models.IntegerField()),
                ('image_Goods', models.ImageField(upload_to='marchent/')),
                ('Goods_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='marchent.goods_type')),
            ],
            options={
                'db_table': 'Image_Goods',
            },
        ),
    ]
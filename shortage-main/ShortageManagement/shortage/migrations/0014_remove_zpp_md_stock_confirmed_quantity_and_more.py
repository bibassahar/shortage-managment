# Generated by Django 4.0.2 on 2022-05-19 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortage', '0013_zpp_md_stock_confirmed_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zpp_md_stock',
            name='confirmed_quantity',
        ),
        migrations.RemoveField(
            model_name='zpp_md_stock',
            name='purchasing_group',
        ),
        migrations.RemoveField(
            model_name='zpp_md_stock',
            name='validated_delivery_date',
        ),
        migrations.RemoveField(
            model_name='zpp_md_stock',
            name='vendor_name',
        ),
    ]
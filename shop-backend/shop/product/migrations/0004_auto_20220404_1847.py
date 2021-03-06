# Generated by Django 3.2.4 on 2022-04-04 10:47

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20220205_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='static/product-images'),
        ),
        migrations.AlterField(
            model_name='productvariants',
            name='productVariant_image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='static/productVariant'),
        ),
    ]

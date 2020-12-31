# Generated by Django 3.1.2 on 2020-12-30 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True),
        ),
    ]
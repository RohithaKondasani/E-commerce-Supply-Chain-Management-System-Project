# Generated by Django 5.0.1 on 2024-03-09 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_productdetails_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/productimages/'),
        ),
    ]
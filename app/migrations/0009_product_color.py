# Generated by Django 4.1.7 on 2023-03-29 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_product_describe'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]

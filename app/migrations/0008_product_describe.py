# Generated by Django 4.1.7 on 2023-03-29 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='describe',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

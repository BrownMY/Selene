# Generated by Django 3.1.7 on 2021-03-31 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
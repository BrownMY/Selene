# Generated by Django 3.1.7 on 2021-04-05 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_product_vidurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catimg',
            field=models.CharField(default=1, max_length=350),
            preserve_default=False,
        ),
    ]

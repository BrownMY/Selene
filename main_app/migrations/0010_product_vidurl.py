# Generated by Django 3.1.7 on 2021-04-02 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20210401_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vidurl',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0004_auto_20201108_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]

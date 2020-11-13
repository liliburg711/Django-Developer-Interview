# Generated by Django 3.1.3 on 2020-11-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0009_auto_20201109_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='discount',
            field=models.CharField(db_index=True, max_length=800),
        ),
        migrations.AlterField(
            model_name='sale',
            name='link',
            field=models.URLField(max_length=800),
        ),
        migrations.AlterField(
            model_name='sale',
            name='price',
            field=models.CharField(db_index=True, max_length=800),
        ),
        migrations.AlterField(
            model_name='sale',
            name='title',
            field=models.CharField(db_index=True, max_length=800),
        ),
    ]
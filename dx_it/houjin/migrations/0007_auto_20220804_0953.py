# Generated by Django 3.1.7 on 2022-08-04 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houjin', '0006_auto_20220804_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='dm_check',
            field=models.BooleanField(default=False, verbose_name='DMリスト'),
        ),
    ]
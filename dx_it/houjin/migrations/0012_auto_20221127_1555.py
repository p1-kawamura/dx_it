# Generated by Django 3.1.7 on 2022-11-27 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houjin', '0011_auto_20221127_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='nouhin_day',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='納品'),
        ),
    ]

# Generated by Django 3.1.7 on 2022-12-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houjin', '0014_auto_20221203_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='bikou',
            field=models.TextField(blank=True, default='', verbose_name='備考'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='bikou2',
            field=models.TextField(blank=True, default='', verbose_name='備考2'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='bikou3',
            field=models.TextField(blank=True, default='', verbose_name='備考3'),
        ),
    ]
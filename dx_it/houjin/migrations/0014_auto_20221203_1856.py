# Generated by Django 3.1.7 on 2022-12-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houjin', '0013_auto_20221127_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='bikou2',
            field=models.TextField(blank=True, null=True, verbose_name='備考2'),
        ),
        migrations.AddField(
            model_name='customer',
            name='bikou3',
            field=models.TextField(blank=True, null=True, verbose_name='備考3'),
        ),
    ]
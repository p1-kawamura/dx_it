# Generated by Django 3.1.7 on 2022-07-22 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houjin', '0003_auto_20220722_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='tantou',
            field=models.IntegerField(default=0, verbose_name='担当'),
        ),
    ]
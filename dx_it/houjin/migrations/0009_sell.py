# Generated by Django 3.1.7 on 2022-10-26 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houjin', '0008_customer_nohin_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sell_mon', models.CharField(blank=True, max_length=10, null=True, verbose_name='年月')),
                ('sell_money', models.IntegerField(blank=True, null=True, verbose_name='金額')),
                ('sell_cus_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='houjin.customer', verbose_name='顧客ID')),
            ],
        ),
    ]

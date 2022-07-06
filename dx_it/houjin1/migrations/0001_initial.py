# Generated by Django 3.1.7 on 2022-07-06 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_id', models.CharField(blank=True, max_length=10, null=True, verbose_name='顧客ID')),
                ('sei', models.CharField(blank=True, max_length=10, null=True, verbose_name='姓')),
                ('mei', models.CharField(blank=True, max_length=10, null=True, verbose_name='名')),
                ('sei_kana', models.CharField(blank=True, max_length=10, null=True, verbose_name='姓かな')),
                ('mei_kana', models.CharField(blank=True, max_length=10, null=True, verbose_name='名かな')),
                ('mail1', models.EmailField(blank=True, max_length=254, null=True, verbose_name='メール1')),
                ('mail2', models.EmailField(blank=True, max_length=254, null=True, verbose_name='メール2')),
                ('mail3', models.EmailField(blank=True, max_length=254, null=True, verbose_name='メール3')),
                ('yubin', models.CharField(blank=True, max_length=10, null=True, verbose_name='郵便番号')),
                ('adress', models.CharField(blank=True, max_length=100, null=True, verbose_name='住所')),
                ('pref', models.CharField(blank=True, max_length=10, null=True, verbose_name='都道府県')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='市区町村')),
                ('banchi', models.CharField(blank=True, max_length=50, null=True, verbose_name='番地')),
                ('build', models.CharField(blank=True, max_length=50, null=True, verbose_name='建物')),
                ('com', models.CharField(blank=True, max_length=50, null=True, verbose_name='会社')),
                ('busho', models.CharField(blank=True, max_length=50, null=True, verbose_name='部署')),
                ('tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='電話')),
                ('mob', models.CharField(blank=True, max_length=20, null=True, verbose_name='携帯')),
                ('fax', models.CharField(blank=True, max_length=20, null=True, verbose_name='FAX')),
                ('toroku', models.CharField(blank=True, max_length=10, null=True, verbose_name='登録日')),
                ('kensu', models.IntegerField(blank=True, null=True, verbose_name='件数')),
                ('money', models.IntegerField(blank=True, null=True, verbose_name='金額')),
                ('tantou', models.CharField(blank=True, max_length=10, null=True, verbose_name='担当')),
                ('dm_day', models.CharField(blank=True, max_length=10, null=True, verbose_name='DM')),
                ('tel_day', models.CharField(blank=True, max_length=10, null=True, verbose_name='TEL')),
                ('gaisho_day', models.CharField(blank=True, max_length=10, null=True, verbose_name='外商')),
                ('bikou', models.TextField(blank=True, null=True, verbose_name='備考')),
            ],
        ),
        migrations.CreateModel(
            name='Recieve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_id', models.CharField(blank=True, max_length=10, null=True, verbose_name='見積ID')),
                ('rec_no', models.CharField(blank=True, max_length=10, null=True, verbose_name='見積番号')),
                ('rec_ver', models.CharField(blank=True, max_length=10, null=True, verbose_name='バージョン')),
                ('status', models.CharField(blank=True, max_length=10, null=True, verbose_name='ステータス')),
                ('mitsu_day', models.CharField(blank=True, max_length=10, null=True, verbose_name='見積日')),
                ('rec_day', models.CharField(blank=True, max_length=10, null=True, verbose_name='受注日')),
                ('eigyou_sei', models.CharField(blank=True, max_length=10, null=True, verbose_name='担当_姓')),
                ('eigyou_mei', models.CharField(blank=True, max_length=10, null=True, verbose_name='担当_名')),
                ('eigyou_busho', models.CharField(blank=True, max_length=20, null=True, verbose_name='営業部署')),
                ('keiro', models.CharField(blank=True, max_length=10, null=True, verbose_name='流入経路')),
                ('mitsu_money', models.IntegerField(blank=True, null=True, verbose_name='見積金額')),
                ('rec_cus_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='houjin1.customer', verbose_name='顧客ID')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='品名')),
                ('item_rec_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='houjin1.recieve', verbose_name='見積ID')),
            ],
        ),
    ]

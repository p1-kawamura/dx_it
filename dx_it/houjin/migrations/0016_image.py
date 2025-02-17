# Generated by Django 4.2.1 on 2025-01-10 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houjin', '0015_auto_20221203_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image', verbose_name='イメージ図')),
                ('create_day', models.DateTimeField(auto_now=True, verbose_name='作成日')),
            ],
        ),
    ]

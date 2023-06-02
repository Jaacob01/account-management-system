# Generated by Django 3.2.12 on 2023-04-03 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='hoster',
            field=models.PositiveSmallIntegerField(choices=[(1, '本地环境'), (2, '阿里云'), (3, '腾讯云'), (4, '微信云开发'), (5, '微信云托管')], null=True, verbose_name='托管方'),
        ),
    ]
# Generated by Django 3.2.6 on 2021-08-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b_signup', '0003_auto_20210812_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login_ID',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickName',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='passWord',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='school',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

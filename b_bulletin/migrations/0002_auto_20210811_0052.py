# Generated by Django 2.2.3 on 2021-08-10 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b_bulletin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotionpost',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-13 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b_community', '0003_alter_community_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='community/'),
        ),
    ]

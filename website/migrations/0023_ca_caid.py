# Generated by Django 2.1.5 on 2019-06-17 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_auto_20190616_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='ca',
            name='caid',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]

# Generated by Django 2.1.5 on 2019-06-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_ca_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ca',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]

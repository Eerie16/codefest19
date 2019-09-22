# Generated by Django 2.1.5 on 2019-04-20 05:37

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_profile_referral_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(null=True, upload_to=website.models.Profile.get_file_path),
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-07 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_alter_userprofile_bio_alter_userprofile_time_zone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-28 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0013_alter_education_education_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

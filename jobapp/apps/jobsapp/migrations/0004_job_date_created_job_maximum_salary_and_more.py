# Generated by Django 4.2.7 on 2023-12-08 03:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0003_workexperience_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='maximum_salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='minimum_salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]

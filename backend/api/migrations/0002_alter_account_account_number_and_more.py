# Generated by Django 4.1.7 on 2023-02-22 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.CharField(default='8320087734401797', max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='current_balance',
            field=models.FloatField(default=0),
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-26 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_account_account_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.CharField(default='6313817848965267', max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('DEBIT', 'DEBIT'), ('CREDIT', 'CREDIT')], max_length=6),
        ),
    ]

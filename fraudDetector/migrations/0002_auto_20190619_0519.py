# Generated by Django 2.2.2 on 2019-06-19 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fraudDetector', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CreditCards',
            new_name='CreditCard',
        ),
    ]

# Generated by Django 3.0.5 on 2023-04-15 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0005_auto_20230415_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='last_donated',
        ),
        migrations.AddField(
            model_name='blooddonate',
            name='last_donation_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-26 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_allocationtypes_phonebookallocationtypes'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonebookallocationtypes',
            name='default_amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

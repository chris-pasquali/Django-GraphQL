# Generated by Django 4.0.3 on 2022-03-26 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_address_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.CharField(default=-1, max_length=250),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-26 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_address_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(choices=[('NSW', 'New South Wales'), ('VIC', 'Victoria'), ('QLD', 'Queensland'), ('SA', 'South Australia'), ('WA', 'Western Australia'), ('TAS', 'Tasmania'), ('NT', 'Northern Territory'), ('ACT', 'Australian Capital Territory')], default='NSW', max_length=3),
        ),
    ]

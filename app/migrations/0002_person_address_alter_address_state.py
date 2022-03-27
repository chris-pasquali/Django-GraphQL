# Generated by Django 4.0.3 on 2022-03-25 14:09

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.ForeignKey(default=-1.0, on_delete=django.db.models.deletion.CASCADE, to='app.address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(choices=[('NSW', 'New South Wales'), ('VIC', 'Victoria'), ('QLD', 'Queensland'), ('SA', 'South Australia'), ('WA', 'Western Australia'), ('TAS', 'Tasmania'), ('NT', 'Northern Territory'), ('ACT', 'Australian Capital Territory')], default=app.models.StatesEnum['NSW'], max_length=3),
        ),
    ]

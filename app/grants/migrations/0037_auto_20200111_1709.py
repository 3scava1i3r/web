# Generated by Django 2.2.4 on 2020-01-11 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0036_auto_20200110_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='last_clr_calc_date',
            field=models.DateTimeField(blank=True, help_text='The last clr calculation date', null=True),
        ),
        migrations.AddField(
            model_name='grant',
            name='next_clr_calc_date',
            field=models.DateTimeField(blank=True, help_text='The last clr calculation date', null=True),
        ),
    ]

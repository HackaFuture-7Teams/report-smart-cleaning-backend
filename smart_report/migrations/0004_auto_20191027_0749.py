# Generated by Django 2.2 on 2019-10-27 07:49

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart_report', '0003_rawdata_body_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawdata',
            name='body_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]

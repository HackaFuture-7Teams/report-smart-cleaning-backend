# Generated by Django 2.2 on 2019-10-27 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_report', '0002_auto_20191027_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawdata',
            name='body_json',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
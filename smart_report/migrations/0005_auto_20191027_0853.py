# Generated by Django 2.2 on 2019-10-27 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_report', '0004_auto_20191027_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawdata',
            name='receive_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rawdata',
            name='sender_id',
            field=models.CharField(max_length=100),
        ),
    ]
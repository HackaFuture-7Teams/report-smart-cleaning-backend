# Generated by Django 2.2 on 2019-10-27 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart_report', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rawdata',
            old_name='admin_id',
            new_name='receive_id',
        ),
        migrations.RenameField(
            model_name='rawdata',
            old_name='user_id',
            new_name='sender_id',
        ),
    ]
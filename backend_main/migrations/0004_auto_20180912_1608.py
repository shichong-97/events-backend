# Generated by Django 2.0.1 on 2018-09-12 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_main', '0003_auto_20180901_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='num_going',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='num_interested',
        ),
    ]

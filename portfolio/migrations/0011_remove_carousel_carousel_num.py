# Generated by Django 2.1.7 on 2019-03-13 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20190313_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='carousel_num',
        ),
    ]

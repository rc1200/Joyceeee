# Generated by Django 2.1.7 on 2019-03-13 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20190313_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='carousel_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

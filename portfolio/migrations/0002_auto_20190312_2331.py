# Generated by Django 2.1.7 on 2019-03-13 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='is_active',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

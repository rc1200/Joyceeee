# Generated by Django 2.1.7 on 2019-03-13 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_remove_carousel_carousel_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='carousel_num',
            field=models.CharField(blank=True, default='text-right', max_length=20, null=True),
        ),
    ]

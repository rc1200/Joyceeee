# Generated by Django 2.1.7 on 2019-03-13 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20190313_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='button_text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

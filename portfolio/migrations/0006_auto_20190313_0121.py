# Generated by Django 2.1.7 on 2019-03-13 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20190313_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carousel',
            name='carousel_num',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-19 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_carousel_button_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderEmail', models.EmailField(max_length=70, verbose_name='Your Email')),
                ('message', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='carousel',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]

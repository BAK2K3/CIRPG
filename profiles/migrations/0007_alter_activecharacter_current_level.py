# Generated by Django 3.2.4 on 2021-07-18 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20210714_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activecharacter',
            name='current_level',
            field=models.IntegerField(default=1),
        ),
    ]

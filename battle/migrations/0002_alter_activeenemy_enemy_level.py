# Generated by Django 3.2.4 on 2021-07-14 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activeenemy',
            name='enemy_level',
            field=models.IntegerField(default=1),
        ),
    ]
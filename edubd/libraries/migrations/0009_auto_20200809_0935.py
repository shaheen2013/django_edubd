# Generated by Django 3.0.8 on 2020-08-09 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0008_rack'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rack',
            name='subject',
        ),
        migrations.AlterField(
            model_name='rack',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]

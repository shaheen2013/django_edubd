# Generated by Django 3.0.8 on 2020-08-16 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import leave.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leave', '0005_auto_20200816_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='leave',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='leave', validators=[leave.models.validate_file]),
        ),
    ]

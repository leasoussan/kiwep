# Generated by Django 3.1.5 on 2021-08-19 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210808_1616'),
        ('content', '0002_auto_20210818_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.field'),
        ),
    ]

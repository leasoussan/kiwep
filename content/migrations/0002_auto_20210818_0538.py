# Generated by Django 3.1.5 on 2021-08-18 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='points',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.1.5 on 2021-06-01 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20210526_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='due_date',
        ),
    ]
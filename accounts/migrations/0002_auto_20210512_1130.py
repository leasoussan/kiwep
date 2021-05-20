# Generated by Django 3.1.5 on 2021-05-12 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.group'),
        ),
        migrations.AddField(
            model_name='student',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.field'),
        ),
    ]

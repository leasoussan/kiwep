# Generated by Django 3.1.5 on 2021-05-20 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20210519_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='project',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.project'),
        ),
    ]

# Generated by Django 3.1.5 on 2021-08-22 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20210820_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='response_type',
            field=models.CharField(blank=True, choices=[('link', 'link'), ('video', 'video'), ('doc', 'document'), ('power_p', 'power Point'), ('image', 'image')], default=None, max_length=200, null=True),
        ),
    ]

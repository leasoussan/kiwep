# Generated by Django 3.1.5 on 2021-05-30 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20210530_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='image',
            field=models.ImageField(default='media/image/default.png', upload_to='images/'),
        ),
    ]

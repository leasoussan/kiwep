# Generated by Django 3.1.5 on 2021-08-26 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_student_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile/avatar.png', null=True, upload_to='profile'),
        ),
    ]
# Generated by Django 3.1.5 on 2021-11-04 19:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_auto_20211104_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='response_comment',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
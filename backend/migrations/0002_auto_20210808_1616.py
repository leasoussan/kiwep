# Generated by Django 3.1.5 on 2021-08-08 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend', '0001_initial'),
        ('accounts', '0002_auto_20210808_1616'),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsoftskillrating',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.skills'),
        ),
        migrations.AddField(
            model_name='studentsoftskillrating',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student'),
        ),
        migrations.AddField(
            model_name='studentsoftskillrating',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.team'),
        ),
        migrations.AddField(
            model_name='institutioncategory',
            name='fields',
            field=models.ManyToManyField(to='backend.Field'),
        ),
        migrations.AddField(
            model_name='institution',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.institutioncategory'),
        ),
        migrations.AddField(
            model_name='institution',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.field'),
        ),
        migrations.AddField(
            model_name='institution',
            name='representative',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.representative'),
        ),
        migrations.AddField(
            model_name='group',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.institution'),
        ),
    ]

<<<<<<< HEAD:backend/migrations/0002_auto_20210512_1130.py
# Generated by Django 3.1.5 on 2021-05-12 11:30
=======
# Generated by Django 3.1.5 on 2021-05-12 08:28
>>>>>>> add5770bc99ff338cde77c101525c62677dfeafd:backend/migrations/0002_auto_20210512_0828.py

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD:backend/migrations/0002_auto_20210512_1130.py
        ('content', '0001_initial'),
        ('accounts', '0002_auto_20210512_1130'),
        ('backend', '0001_initial'),
=======
        ('backend', '0001_initial'),
        ('accounts', '0001_initial'),
        ('content', '0001_initial'),
>>>>>>> add5770bc99ff338cde77c101525c62677dfeafd:backend/migrations/0002_auto_20210512_0828.py
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
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.field'),
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

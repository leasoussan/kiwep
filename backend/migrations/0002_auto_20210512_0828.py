
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [

        ('backend', '0001_initial'),
        ('accounts', '0001_initial'),
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

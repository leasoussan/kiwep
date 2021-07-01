# Generated by Django 3.1.5 on 2021-07-01 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20210701_0919'),
        ('content', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('backend', '0002_auto_20210701_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='softs_skills',
            field=models.ManyToManyField(related_name='student_skills_scores', through='backend.StudentSoftSkillRating', to='content.Skills'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='speakerinvite',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.institution'),
        ),
        migrations.AddField(
            model_name='speakerinvite',
            name='joined_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_invites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='speakerinvite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='invitor'),
        ),
        migrations.AddField(
            model_name='speaker',
            name='group',
            field=models.ManyToManyField(to='backend.Group'),
        ),
        migrations.AddField(
            model_name='speaker',
            name='institution',
            field=models.ManyToManyField(to='backend.Institution'),
        ),
        migrations.AddField(
            model_name='speaker',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='representative',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='institutioninvite',
            name='joined_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_platform_invites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='institutioninvite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='invitor'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.country'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.city'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]

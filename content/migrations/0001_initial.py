# Generated by Django 3.1.5 on 2021-04-01 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('backend', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('stage', models.CharField(choices=[('start', 'Start'), ('middle', 'Middle'), ('final', 'Final')], default='start', max_length=10)),
                ('description', models.TextField()),
                ('points', models.PositiveIntegerField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.field')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.level')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('time_to_complet', models.PositiveIntegerField()),
                ('completed', models.BooleanField(default=False)),
                ('points', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('due_date', models.DateField()),
                ('project_completed', models.BooleanField(blank=True, null=True)),
                ('group_Institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.group')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_manager', to='accounts.speaker')),
            ],
        ),
        migrations.CreateModel(
            name='TeamProjectMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('completed', models.BooleanField(default=False)),
                ('response_text', models.TextField(blank=True)),
                ('response_file', models.FileField(blank=True, null=True, upload_to='')),
                ('accepted', models.BooleanField(default=False)),
                ('attributed_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_missions', to='accounts.student')),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.mission')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='missions',
            field=models.ManyToManyField(through='content.TeamProjectMission', to='content.Mission'),
        ),
        migrations.AddField(
            model_name='team',
            name='participants',
            field=models.ManyToManyField(blank=True, to='accounts.Student'),
        ),
        migrations.AddField(
            model_name='team',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.project'),
        ),
        migrations.CreateModel(
            name='SkillsAcquired',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('points', models.PositiveIntegerField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.subjects')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('image', models.ImageField(default='image/default.png', upload_to='images/')),
                ('file_rsc', models.FileField(blank=True, null=True, upload_to='')),
                ('text', models.TextField()),
                ('field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.field')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequiredSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.subjects')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='acquried_skils',
            field=models.ManyToManyField(blank=True, to='content.SkillsAcquired'),
        ),
        migrations.AddField(
            model_name='project',
            name='difficulty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.level'),
        ),
        migrations.AddField(
            model_name='project',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.field'),
        ),
        migrations.AddField(
            model_name='project',
            name='mission',
            field=models.ManyToManyField(blank=True, to='content.Mission'),
        ),
        migrations.AddField(
            model_name='project',
            name='required_skills',
            field=models.ManyToManyField(blank=True, to='content.RequiredSkills'),
        ),
        migrations.AddField(
            model_name='project',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.speaker'),
        ),
        migrations.AddField(
            model_name='mission',
            name='resources',
            field=models.ManyToManyField(to='content.Resource'),
        ),
    ]
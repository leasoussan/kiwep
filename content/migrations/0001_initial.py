# Generated by Django 3.1.5 on 2021-05-26 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('accounts', '0002_auto_20210526_0848'),
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectiveMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(choices=[('start', 'Start'), ('middle', 'Middle'), ('final', 'Final')], default='start', max_length=10)),
                ('response_type', models.CharField(choices=[('link', 'Link'), ('video', 'Video'), ('doc', 'Document'), ('power_p', 'Power Point'), ('image', 'image')], default=None, max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('points', models.PositiveIntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HardSkillsRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('time_to_complete', models.PositiveIntegerField()),
                ('completed', models.BooleanField(default=False)),
                ('points', models.PositiveIntegerField()),
                ('is_template', models.BooleanField(default=False)),
                ('is_global', models.BooleanField(default=False)),
                ('is_premium', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
            },
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
                ('participants', models.ManyToManyField(blank=True, to='accounts.Student')),
                ('project', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.project')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('field', models.ManyToManyField(to='backend.Field')),
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
        migrations.AddField(
            model_name='project',
            name='acquired_skills',
            field=models.ManyToManyField(to='content.Skills'),
        ),
        migrations.AddField(
            model_name='project',
            name='difficulty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.level'),
        ),
        migrations.AddField(
            model_name='project',
            name='field',
            field=models.ManyToManyField(to='backend.Field'),
        ),
        migrations.AddField(
            model_name='project',
            name='required_skills',
            field=models.ManyToManyField(related_name='required_skills', to='content.Skills'),
        ),
        migrations.AddField(
            model_name='project',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.speaker'),
        ),
        migrations.CreateModel(
            name='MissionValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activity_logs', to='contenttypes.contenttype')),
                ('hard_skills', models.ManyToManyField(blank=True, through='content.HardSkillsRating', to='content.Skills')),
            ],
        ),
        migrations.CreateModel(
            name='IndividualMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(choices=[('start', 'Start'), ('middle', 'Middle'), ('final', 'Final')], default='start', max_length=10)),
                ('response_type', models.CharField(choices=[('link', 'Link'), ('video', 'Video'), ('doc', 'Document'), ('power_p', 'Power Point'), ('image', 'image')], default=None, max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('points', models.PositiveIntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('completed', models.BooleanField(default=False)),
                ('response_comment', models.TextField(blank=True)),
                ('response_file', models.FileField(blank=True, null=True, upload_to='')),
                ('accepted', models.BooleanField(default=False)),
                ('acquired_skill', models.ManyToManyField(blank=True, to='content.Skills')),
                ('attributed_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_missions', to='accounts.student')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.field')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.level')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.project')),
                ('resources', models.ManyToManyField(to='content.Resource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndividualCollectiveMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(choices=[('start', 'Start'), ('middle', 'Middle'), ('final', 'Final')], default='start', max_length=10)),
                ('response_type', models.CharField(choices=[('link', 'Link'), ('video', 'Video'), ('doc', 'Document'), ('power_p', 'Power Point'), ('image', 'image')], default=None, max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('points', models.PositiveIntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('completed', models.BooleanField(default=False)),
                ('response_comment', models.TextField(blank=True)),
                ('response_file', models.FileField(blank=True, null=True, upload_to='')),
                ('accepted', models.BooleanField(default=False)),
                ('acquired_skill', models.ManyToManyField(blank=True, to='content.Skills')),
                ('attributed_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='individual_team_mission', to='accounts.student')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.field')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.level')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent_mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.collectivemission')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.project')),
                ('resources', models.ManyToManyField(to='content.Resource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='hardskillsrating',
            name='project_mission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.missionvalue'),
        ),
        migrations.AddField(
            model_name='hardskillsrating',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.skills'),
        ),
        migrations.AddField(
            model_name='collectivemission',
            name='acquired_skill',
            field=models.ManyToManyField(blank=True, to='content.Skills'),
        ),
        migrations.AddField(
            model_name='collectivemission',
            name='attributed_to',
            field=models.ManyToManyField(blank=True, related_name='my_team_missions', through='content.IndividualCollectiveMission', to='accounts.Student'),
        ),
        migrations.AddField(
            model_name='collectivemission',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.field'),
        ),
        migrations.AddField(
            model_name='collectivemission',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.level'),
        ),
        migrations.AddField(
            model_name='collectivemission',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='collectivemission',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.project'),
        ),
        migrations.AddField(
            model_name='collectivemission',
            name='resources',
            field=models.ManyToManyField(to='content.Resource'),
        ),
    ]

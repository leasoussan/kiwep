<<<<<<< HEAD
# Generated by Django 3.1.5 on 2021-05-12 11:30
=======
# Generated by Django 3.1.5 on 2021-05-12 08:28
>>>>>>> add5770bc99ff338cde77c101525c62677dfeafd

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('content', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20210512_1130'),
=======
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0001_initial'),
>>>>>>> add5770bc99ff338cde77c101525c62677dfeafd
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('details', models.CharField(max_length=50)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalTask',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='todo.task')),
                ('completed', models.BooleanField(default=False)),
            ],
            bases=('todo.task',),
        ),
        migrations.CreateModel(
            name='StudentTeamTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
        ),
        migrations.CreateModel(
            name='TeamTask',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='todo.task')),
                ('assignees', models.ManyToManyField(blank=True, through='todo.StudentTeamTask', to='accounts.Student')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.team')),
            ],
            bases=('todo.task',),
        ),
        migrations.AddField(
            model_name='studentteamtask',
            name='team_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.teamtask'),
        ),
        migrations.CreateModel(
            name='AssignedTask',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='todo.task')),
                ('completed', models.BooleanField(default=False)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
            bases=('todo.task',),
        ),
    ]

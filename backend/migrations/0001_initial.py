# Generated by Django 3.1.5 on 2021-07-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('skills_type', models.CharField(choices=[('soft', 'Soft Skills'), ('hard', 'Hard Skills')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number_of_participants', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(blank=True, default='profile/avatar.png', null=True, upload_to='media/profile/')),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('joined_date', models.DateField(auto_now_add=True)),
                ('website', models.URLField()),
                ('description', models.TextField()),
                ('join_code', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentSoftSkillRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('comment', models.TextField()),
            ],
        ),
    ]

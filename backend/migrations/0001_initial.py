# Generated by Django 3.1.5 on 2021-04-01 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
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
            name='InstitutionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fields', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.field')),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(upload_to='')),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('joined_date', models.DateField(auto_now_add=True)),
                ('contact_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.institutioncategory')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.field')),
                ('representative', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.representative')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number_of_participants', models.PositiveIntegerField()),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.institution')),
            ],
        ),
    ]
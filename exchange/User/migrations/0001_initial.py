# Generated by Django 5.0.1 on 2024-01-10 04:22

import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('role', models.CharField(choices=[('C', 'customer'), ('F', 'freelancer')], max_length=100, null=True)),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
                ('first_name', models.CharField(max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='first name')),
                ('last_name', models.CharField(max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='last name')),
                ('country', models.CharField(max_length=100, verbose_name='country')),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now, verbose_name='date of birth')),
                ('joining_date', models.DateField(default=django.utils.timezone.now, verbose_name='joining date')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]

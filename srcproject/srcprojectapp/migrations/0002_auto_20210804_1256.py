# Generated by Django 3.2.6 on 2021-08-04 07:26

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('srcprojectapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadGenerator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_name', models.CharField(max_length=200)),
                ('lead_source', models.CharField(max_length=300)),
                ('lead_user_email', models.EmailField(max_length=300)),
                ('lead_created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='lead created')),
            ],
            options={
                'verbose_name': 'Lead Generator',
                'verbose_name_plural': 'Lead Generators',
            },
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mob_number',
            field=models.CharField(default=432, error_messages={'unique': 'A user with that phone number address already exists'}, max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid international mobile phone number ', regex='^(?:[0-9]●?){6,14}[0-9]$')], verbose_name='Phone Number '),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-09 12:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=100, null=True)),
                ('alternate_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Alternate email address')),
                ('mobile', models.CharField(blank=True, help_text='e.g. +1234567890', max_length=25, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+\\d+')])),
                ('sites', models.ManyToManyField(blank=True, to='sites.Site')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

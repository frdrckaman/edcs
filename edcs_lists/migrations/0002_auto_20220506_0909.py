# Generated by Django 3.1.7 on 2022-05-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_lists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmokingTobaccoProducts',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Smoking Tobacco Products',
                'verbose_name_plural': 'Smoking Tobacco Products',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='TobaccoProducts',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Tobacco Products',
                'verbose_name_plural': 'Tobacco Products',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.AddIndex(
            model_name='tobaccoproducts',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='edcs_lists__id_d73cec_idx'),
        ),
        migrations.AddIndex(
            model_name='smokingtobaccoproducts',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='edcs_lists__id_cff774_idx'),
        ),
    ]

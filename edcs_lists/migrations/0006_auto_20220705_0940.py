# Generated by Django 3.1.7 on 2022-07-05 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_lists', '0005_auto_20220518_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirMonitorProblem',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Air Monitor Problem',
                'verbose_name_plural': 'Air Monitor Problem',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='CookingArea',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Cooking Area',
                'verbose_name_plural': 'Cooking Area',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='CookingDone',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Cooking Done',
                'verbose_name_plural': 'Cooking Done',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='CookingFuel',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Cooking Fuel',
                'verbose_name_plural': 'Cooking Fuel',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='OtherCookingFuel',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Other Cooking Fuel',
                'verbose_name_plural': 'Other Cooking Fuel',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='SolidFuel',
            fields=[
                ('name', models.CharField(db_index=True, help_text='This is the stored value, required', max_length=250, unique=True, verbose_name='Stored value')),
                ('display_name', models.CharField(db_index=True, help_text='(suggest 40 characters max.)', max_length=250, unique=True, verbose_name='Name')),
                ('display_index', models.IntegerField(db_index=True, default=0, help_text='Index to control display order if not alphabetical, not required', verbose_name='display index')),
                ('field_name', models.CharField(blank=True, editable=False, help_text='Not required', max_length=25, null=True)),
                ('version', models.CharField(default='1.0', editable=False, max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Solid Fuel',
                'verbose_name_plural': 'Solid Fuel',
                'ordering': ['display_index', 'display_name'],
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
        ),
        migrations.AddIndex(
            model_name='solidfuel',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='edcs_lists__id_d7e1a0_idx'),
        ),
        migrations.AddIndex(
            model_name='othercookingfuel',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='edcs_lists__id_802526_idx'),
        ),
        migrations.AddIndex(
            model_name='cookingfuel',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='edcs_lists__id_00b214_idx'),
        ),
        migrations.AddIndex(
            model_name='cookingdone',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='edcs_lists__id_dd41d1_idx'),
        ),
        migrations.AddIndex(
            model_name='cookingarea',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='edcs_lists__id_9f3a5e_idx'),
        ),
        migrations.AddIndex(
            model_name='airmonitorproblem',
            index=models.Index(fields=['id', 'display_name', 'display_index'], name='edcs_lists__id_a286bd_idx'),
        ),
    ]
# Generated by Django 3.1.7 on 2021-04-29 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_rab002', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demographic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_initials', models.CharField(max_length=3)),
                ('subject_id', models.CharField(max_length=9)),
                ('visit_date', models.DateField()),
                ('visit_code', models.CharField(choices=[('1', 'sc1')], max_length=1)),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female')], max_length=1)),
                ('race', models.CharField(choices=[('1', 'Africa'), ('2', 'Others')], max_length=1)),
                ('dob', models.DateField()),
                ('years', models.IntegerField()),
                ('months', models.IntegerField()),
                ('residence', models.CharField(choices=[('1', 'Bagamoyo town'), ('2', 'Nearby district')], max_length=1)),
                ('phone', models.IntegerField()),
                ('literate', models.CharField(choices=[('1', 'Yes'), ('2', 'No'), ('3', 'N/A')], max_length=1)),
                ('education', models.CharField(choices=[('1', 'Primary'), ('2', 'Secondary'), ('3', 'College'), ('4', 'Non-Formal'), ('5', 'N/A')], max_length=1)),
                ('address', models.TextField(editable=False)),
                ('coordinator_initials', models.CharField(max_length=3)),
                ('coordinator_time', models.TimeField()),
                ('reviewer_initials', models.CharField(max_length=3)),
                ('reviewer_time', models.TimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]
# Generated by Django 3.1.7 on 2024-03-05 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_screening', '0004_auto_20240305_1727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalsubjectscreening',
            old_name='other_cancer',
            new_name='other_cancer_dx',
        ),
        migrations.RenameField(
            model_name='subjectscreening',
            old_name='other_cancer',
            new_name='other_cancer_dx',
        ),
    ]

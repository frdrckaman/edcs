# Generated by Django 3.1.7 on 2024-03-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_subject', '0053_auto_20240305_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicalreview',
            name='tb_dx',
            field=models.CharField(choices=[('yes_clinically', 'Yes clinically'), ('Yes_bacteriologically', 'Yes bacteriologically confirmed'), ('No', 'No')], max_length=65, null=True, verbose_name='Have you ever been diagnosed with TB?'),
        ),
        migrations.AlterField(
            model_name='historicalclinicalreview',
            name='tb_dx',
            field=models.CharField(choices=[('yes_clinically', 'Yes clinically'), ('Yes_bacteriologically', 'Yes bacteriologically confirmed'), ('No', 'No')], max_length=65, null=True, verbose_name='Have you ever been diagnosed with TB?'),
        ),
    ]

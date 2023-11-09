# Generated by Django 3.1.7 on 2023-11-09 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_subject', '0050_auto_20230724_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpreairquality',
            name='cartridge_number',
            field=models.CharField(max_length=45, null=True, verbose_name='Cartridge Number'),
        ),
        migrations.AddField(
            model_name='historicalpreairquality',
            name='filter_number',
            field=models.CharField(max_length=45, null=True, verbose_name='Filter Number'),
        ),
        migrations.AddField(
            model_name='historicalpreairquality',
            name='upas_number',
            field=models.CharField(max_length=45, null=True, verbose_name='UPAS Number'),
        ),
        migrations.AddField(
            model_name='preairquality',
            name='cartridge_number',
            field=models.CharField(max_length=45, null=True, verbose_name='Cartridge Number'),
        ),
        migrations.AddField(
            model_name='preairquality',
            name='filter_number',
            field=models.CharField(max_length=45, null=True, verbose_name='Filter Number'),
        ),
        migrations.AddField(
            model_name='preairquality',
            name='upas_number',
            field=models.CharField(max_length=45, null=True, verbose_name='UPAS Number'),
        ),
    ]

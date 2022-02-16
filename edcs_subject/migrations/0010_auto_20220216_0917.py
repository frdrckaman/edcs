# Generated by Django 3.1.7 on 2022-02-16 09:17

from django.db import migrations
import edcs_model.models.fields.other_charfield


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_subject', '0009_auto_20220215_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airpollutionfollowup',
            old_name='who_had_illness',
            new_name='fuel_type_used',
        ),
        migrations.RenameField(
            model_name='airpollutionfollowup',
            old_name='fuel_before_changing',
            new_name='stove_type_used',
        ),
        migrations.RenameField(
            model_name='historicalairpollutionfollowup',
            old_name='who_had_illness',
            new_name='fuel_type_used',
        ),
        migrations.RenameField(
            model_name='historicalairpollutionfollowup',
            old_name='fuel_before_changing',
            new_name='stove_type_used',
        ),
        migrations.AddField(
            model_name='airpollutionfollowup',
            name='fuel_type_used_other',
            field=edcs_model.models.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If other, please specify ...'),
        ),
        migrations.AddField(
            model_name='airpollutionfollowup',
            name='stove_type_used_other',
            field=edcs_model.models.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If other, please specify ...'),
        ),
        migrations.AddField(
            model_name='historicalairpollutionfollowup',
            name='fuel_type_used_other',
            field=edcs_model.models.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If other, please specify ...'),
        ),
        migrations.AddField(
            model_name='historicalairpollutionfollowup',
            name='stove_type_used_other',
            field=edcs_model.models.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If other, please specify ...'),
        ),
    ]
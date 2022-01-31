# Generated by Django 3.1.7 on 2022-01-31 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_subject', '0010_auto_20220128_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='airpollutionfollowup',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='airpollutionfollowup',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='alcoholtobaccouse',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='alcoholtobaccouse',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='contraceptiveusereproductivehistory',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='contraceptiveusereproductivehistory',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='cookingfuel',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='cookingfuel',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='covidinfectionhistory',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='covidinfectionhistory',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='demographiccharacteristic',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='demographiccharacteristic',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='effectairpollution',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='effectairpollution',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='historicalairpollutionfollowup',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='historicalairpollutionfollowup',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='historicalalcoholtobaccouse',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='historicalalcoholtobaccouse',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='historicalcontraceptiveusereproductivehistory',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='historicalcontraceptiveusereproductivehistory',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='historicalcookingfuel',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='historicalcookingfuel',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='historicalcovidinfectionhistory',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='historicalcovidinfectionhistory',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='historicaldemographiccharacteristic',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='historicaldemographiccharacteristic',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='historicaleffectairpollution',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='historicaleffectairpollution',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='historicalhivlabinvestigation',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='historicalhivlabinvestigation',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='historicalhomelocatorform',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='historicalhomelocatorform',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='historicalhousekitchensurrounding',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='historicalhousekitchensurrounding',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='historicallungcancerlabinvestigation',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='historicallungcancerlabinvestigation',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='historicallungcancertreatment',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='historicallungcancertreatment',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='historicaloccupationalhistory',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='historicaloccupationalhistory',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='historicalsignsymptomlungcancer',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='historicalsignsymptomlungcancer',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='hivlabinvestigation',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='hivlabinvestigation',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='homelocatorform',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='homelocatorform',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='housekitchensurrounding',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='housekitchensurrounding',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='lungcancerlabinvestigation',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='lungcancerlabinvestigation',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='lungcancertreatment',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='lungcancertreatment',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='occupationalhistory',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='occupationalhistory',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddField(
            model_name='signsymptomlungcancer',
            name='crf_status',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete (some data pending)'), ('COMPLETE', 'Complete')], default='INCOMPLETE', help_text='If some data is still pending, flag this CRF as incomplete', max_length=25, verbose_name='CRF status'),
        ),
        migrations.AddField(
            model_name='signsymptomlungcancer',
            name='crf_status_comments',
            field=models.TextField(blank=True, help_text='for example, why some data is still pending', null=True, verbose_name='Any comments related to status of this CRF'),
        ),
        migrations.AddIndex(
            model_name='clinicalreview',
            index=models.Index(fields=['subject_visit', 'site', 'id'], name='edcs_subjec_subject_ff9b85_idx'),
        ),
    ]

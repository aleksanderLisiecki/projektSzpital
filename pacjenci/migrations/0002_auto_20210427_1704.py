# Generated by Django 3.2 on 2021-04-27 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacjenci', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dicom',
            options={'verbose_name_plural': 'DICOM'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name_plural': 'Patients'},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name_plural': 'Series'},
        ),
        migrations.AlterModelOptions(
            name='studies',
            options={'verbose_name_plural': 'Studies'},
        ),
        migrations.AddField(
            model_name='dicom',
            name='instance',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

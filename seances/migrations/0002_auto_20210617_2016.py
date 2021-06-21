# Generated by Django 3.1.7 on 2021-06-17 19:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('seances', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seance',
            name='dateDebut',
        ),
        migrations.RemoveField(
            model_name='seance',
            name='dateFin',
        ),
        migrations.AddField(
            model_name='seance',
            name='HeureDebut',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seance',
            name='HeureFin',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seance',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
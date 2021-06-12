# Generated by Django 3.2.3 on 2021-05-31 21:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_FD', '0008_auto_20210528_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='these',
            name='doctorant',
        ),
        migrations.AddField(
            model_name='doctorant',
            name='choix',
            field=models.ManyToManyField(to='gestion_FD.These'),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_deliberation',
            field=models.DateField(default=datetime.datetime(2021, 5, 31, 22, 39, 31, 92116)),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_inscription',
            field=models.DateField(default=datetime.datetime(2021, 5, 31, 22, 39, 31, 92116)),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_naissance',
            field=models.DateField(default=datetime.datetime(2021, 5, 31, 22, 39, 31, 92116)),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_reinscription',
            field=models.DateField(default=datetime.datetime(2021, 5, 31, 22, 39, 31, 92116)),
        ),
        migrations.AlterField(
            model_name='employe',
            name='date_naissance',
            field=models.DateField(default=datetime.datetime(2021, 5, 31, 22, 39, 31, 92116)),
        ),
        migrations.AlterField(
            model_name='eval_module',
            name='date_eval',
            field=models.DateField(default=datetime.datetime(2021, 5, 31, 22, 39, 31, 92116)),
        ),
        migrations.AlterField(
            model_name='fiche_evaluation',
            name='date_eval',
            field=models.DateField(default=datetime.datetime(2021, 5, 31, 22, 39, 31, 92116)),
        ),
        migrations.AlterField(
            model_name='pv',
            name='date_pv',
            field=models.DateField(default=datetime.datetime(2021, 5, 31, 22, 39, 31, 92116)),
        ),
    ]

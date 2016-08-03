# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Awaria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('description', models.TextField(verbose_name='Opis awarii', blank=True)),
                ('add_date', models.DateTimeField(verbose_name='Data zgłoszenia', auto_now_add=True)),
                ('repair_date', models.DateTimeField(verbose_name='Data rozpoczęcia naprawy', null=True, blank=True)),
                ('remove_date', models.DateTimeField(verbose_name='Data zakończenia naprawy', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Awaria',
                'verbose_name_plural': 'Awarie',
            },
        ),
        migrations.CreateModel(
            name='Hala',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('symbol', models.CharField(verbose_name='Symbol hali', max_length=10)),
                ('user', models.ForeignKey(verbose_name='Opiekun', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Hala',
                'verbose_name_plural': 'Hale',
            },
        ),
        migrations.CreateModel(
            name='Maszyna',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nazwa', models.CharField(verbose_name='Nazwa', max_length=50)),
                ('hala', models.ForeignKey(verbose_name='Hala', to='failure.Hala')),
                ('opiekun', models.ForeignKey(verbose_name='Opiekun', default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Maszyna',
                'verbose_name_plural': 'Maszyny',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nazwa', models.CharField(verbose_name='Nazwa', max_length=50)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Statusy',
            },
        ),
        migrations.CreateModel(
            name='Wydzial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nazwa', models.CharField(verbose_name='Nazwa wydziału', max_length=50)),
                ('user', models.ForeignKey(verbose_name='Mistrz', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Wydział',
                'verbose_name_plural': 'Wydziały',
            },
        ),
        migrations.AddField(
            model_name='maszyna',
            name='wydzial',
            field=models.ForeignKey(verbose_name='Wydział', to='failure.Wydzial'),
        ),
        migrations.AddField(
            model_name='awaria',
            name='maszyna',
            field=models.ForeignKey(verbose_name='Maszyna', to='failure.Maszyna', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='awaria',
            name='status',
            field=models.ForeignKey(verbose_name='Status', default=1, to='failure.Status'),
        ),
        migrations.AddField(
            model_name='awaria',
            name='sur',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Przyjęte przez', to=settings.AUTH_USER_MODEL, related_name='awaria_sure'),
        ),
        migrations.AddField(
            model_name='awaria',
            name='user',
            field=models.ForeignKey(verbose_name='Zgłaszający', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='awaria',
            name='wydzial',
            field=models.ForeignKey(verbose_name='Wydział', to='failure.Wydzial'),
        ),
    ]

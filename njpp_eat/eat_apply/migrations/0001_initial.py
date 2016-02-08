# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('total_income', models.IntegerField()),
                ('work_income', models.IntegerField()),
                ('assitance_income', models.IntegerField()),
                ('other_income', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_address_one', models.CharField(max_length=200)),
                ('contact_address_two', models.CharField(max_length=200)),
                ('contact_city', models.CharField(max_length=50)),
                ('contact_state', models.CharField(max_length=2)),
                ('contact_zip', models.CharField(max_length=10)),
                ('contact_phone', models.CharField(max_length=10)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_name_of_filer', models.CharField(max_length=200)),
                ('date_completed', models.DateTimeField()),
                ('participate_assistance', models.BooleanField()),
                ('assistance_case_number', models.CharField(max_length=50)),
                ('total_child_income', models.IntegerField()),
                ('total_adult_income', models.IntegerField()),
                ('total_adult_income_wages', models.IntegerField()),
                ('total_adult_income_assistance', models.IntegerField()),
                ('total_adult_income_other', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('middle_initial', models.CharField(max_length=1)),
                ('student', models.BooleanField()),
                ('foster_child', models.BooleanField()),
                ('homless', models.BooleanField()),
                ('total_income', models.IntegerField()),
                ('work_income', models.IntegerField()),
                ('assitance_income', models.IntegerField()),
                ('other_income', models.IntegerField()),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eat_apply.Application')),
            ],
        ),
        migrations.AddField(
            model_name='adult',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eat_apply.Application'),
        ),
    ]

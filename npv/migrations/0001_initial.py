# Generated by Django 5.0.1 on 2024-01-21 14:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('discount_rate', models.FloatField()),
                ('note', models.CharField(max_length=200)),
                ('number_of_projects', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('initial_investment', models.FloatField()),
                ('period', models.IntegerField()),
                ('npv', models.FloatField(blank=True, null=True)),
                ('payback_period', models.IntegerField(blank=True, null=True)),
                ('annualized_npv', models.FloatField(blank=True, null=True)),
                ('consider_further', models.CharField(choices=[('yes', 'Yes'), ('rejected', 'Rejected')], default='yes', max_length=10)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='npv.evaluation')),
            ],
        ),
        migrations.CreateModel(
            name='CashFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('amount', models.FloatField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='npv.project')),
            ],
        ),
    ]

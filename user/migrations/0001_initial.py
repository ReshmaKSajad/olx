# Generated by Django 4.1 on 2022-09-14 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('registration_year', models.PositiveIntegerField(default=1)),
                ('variant', models.CharField(max_length=200)),
                ('owner', models.CharField(max_length=200)),
                ('fuel', models.CharField(max_length=200)),
                ('kilometres', models.PositiveIntegerField(default=1)),
                ('gear_type', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField(default=1)),
                ('colour', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('posted_date', models.CharField(max_length=200)),
            ],
        ),
    ]

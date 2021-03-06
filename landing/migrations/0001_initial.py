# Generated by Django 3.0.3 on 2020-04-09 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiData',
            fields=[
                ('city_name', models.CharField(max_length=90, primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pressure', models.DecimalField(decimal_places=2, max_digits=6)),
                ('wind_speed', models.DecimalField(decimal_places=2, max_digits=6)),
                ('weather_cdn', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'api_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=10)),
                ('starttime', models.TimeField(db_column='startTime')),
                ('endtime', models.TimeField(db_column='endTime')),
                ('message', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'events',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Historical',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('min_humidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('max_humidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('avg_humidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('min_temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('max_temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('avg_temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('min_wind_speed', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max_wind_speed', models.DecimalField(decimal_places=2, max_digits=6)),
                ('avg_wind_speed', models.DecimalField(decimal_places=2, max_digits=6)),
                ('min_pressure', models.DecimalField(decimal_places=0, max_digits=6)),
                ('max_pressure', models.DecimalField(decimal_places=0, max_digits=6)),
                ('avg_pressure', models.DecimalField(decimal_places=0, max_digits=6)),
            ],
            options={
                'db_table': 'historical',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('ip', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'pi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PiData',
            fields=[
                ('pi_id', models.PositiveIntegerField()),
                ('time', models.DateTimeField(primary_key=True, serialize=False)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('wind_speed', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pressure', models.DecimalField(decimal_places=0, max_digits=6)),
            ],
            options={
                'db_table': 'pi_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ThinData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pi_id', models.PositiveIntegerField()),
                ('time', models.DateTimeField()),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('wind_speed', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pressure', models.DecimalField(decimal_places=0, max_digits=6)),
            ],
            options={
                'db_table': 'thin_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=64, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GatheredData',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='gathered_data_id', serialize=False, to='landing.Pi')),
            ],
            options={
                'db_table': 'gathered_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Naming',
            fields=[
                ('email', models.OneToOneField(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='naming_email', serialize=False, to='landing.User')),
            ],
            options={
                'db_table': 'naming',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SignificantApi',
            fields=[
                ('city_name', models.OneToOneField(db_column='city_name', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='significant_api_city_name', serialize=False, to='landing.ApiData')),
            ],
            options={
                'db_table': 'significant_api',
                'managed': False,
            },
        ),
    ]

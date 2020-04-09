# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApiData(models.Model):
    city_name = models.CharField(primary_key=True, max_length=90)
    time = models.DateTimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    pressure = models.DecimalField(max_digits=6, decimal_places=2)
    wind_speed = models.DecimalField(max_digits=6, decimal_places=2)
    weather_cdn = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'api_data'
        unique_together = (('city_name', 'time'),)


class Events(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    type = models.CharField(max_length=10)
    starttime = models.TimeField(db_column='startTime')  # Field name made lowercase.
    endtime = models.TimeField(db_column='endTime')  # Field name made lowercase.
    message = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'events'
        unique_together = (('id', 'type', 'starttime', 'endtime'),)


class GatheredData(models.Model):
    id = models.OneToOneField('Pi', models.DO_NOTHING, db_column='id', primary_key=True)
    pi = models.ForeignKey('PiData', models.DO_NOTHING)
    latitude = models.ForeignKey('Pi', models.DO_NOTHING, db_column='latitude')
    longitude = models.ForeignKey('Pi', models.DO_NOTHING, db_column='longitude')
    date = models.ForeignKey('PiData', models.DO_NOTHING, db_column='date')

    class Meta:
        managed = False
        db_table = 'gathered_data'
        unique_together = (('id', 'latitude', 'longitude'),)


class Historical(models.Model):
    pi = models.ForeignKey('Pi', models.DO_NOTHING)
    date = models.DateField(primary_key=True)
    min_humidity = models.DecimalField(max_digits=5, decimal_places=2)
    max_humidity = models.DecimalField(max_digits=5, decimal_places=2)
    avg_humidity = models.DecimalField(max_digits=5, decimal_places=2)
    min_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    max_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    avg_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    min_wind_speed = models.DecimalField(max_digits=6, decimal_places=2)
    max_wind_speed = models.DecimalField(max_digits=6, decimal_places=2)
    avg_wind_speed = models.DecimalField(max_digits=6, decimal_places=2)
    min_pressure = models.DecimalField(max_digits=6, decimal_places=0)
    max_pressure = models.DecimalField(max_digits=6, decimal_places=0)
    avg_pressure = models.DecimalField(max_digits=6, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'historical'
        unique_together = (('date', 'pi'),)


class Naming(models.Model):
    email = models.OneToOneField('User', models.DO_NOTHING, db_column='email', primary_key=True)
    id = models.ForeignKey('Pi', models.DO_NOTHING, db_column='id')
    latitude = models.ForeignKey('Pi', models.DO_NOTHING, db_column='latitude')
    longitude = models.ForeignKey('Pi', models.DO_NOTHING, db_column='longitude')

    class Meta:
        managed = False
        db_table = 'naming'


class Pi(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    ip = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'pi'
        unique_together = (('id', 'latitude', 'longitude'),)


class PiData(models.Model):
    pi_id = models.PositiveIntegerField()
    time = models.DateTimeField(primary_key=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    wind_speed = models.DecimalField(max_digits=6, decimal_places=2)
    pressure = models.DecimalField(max_digits=6, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'pi_data'


class SignificantApi(models.Model):
    id = models.ForeignKey(Events, models.DO_NOTHING, db_column='id')
    city_name = models.OneToOneField(ApiData, models.DO_NOTHING, db_column='city_name', primary_key=True)
    date = models.ForeignKey(ApiData, models.DO_NOTHING, db_column='date')
    type = models.ForeignKey(Events, models.DO_NOTHING, db_column='type')
    starttime = models.ForeignKey(Events, models.DO_NOTHING, db_column='startTime')  # Field name made lowercase.
    endtime = models.ForeignKey(Events, models.DO_NOTHING, db_column='endTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'significant_api'
        unique_together = (('city_name', 'date'),)


class ThinData(models.Model):
    pi_id = models.PositiveIntegerField()
    time = models.DateTimeField()
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    wind_speed = models.DecimalField(max_digits=6, decimal_places=2)
    pressure = models.DecimalField(max_digits=6, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'thin_data'
        unique_together = (('pi_id', 'time'),)


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(primary_key=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'user'

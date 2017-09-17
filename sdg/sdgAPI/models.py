# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Goal(models.Model):
    id_goal = models.AutoField(primary_key=True)
    goal_number = models.DecimalField(max_digits=65535, decimal_places=65535)
    goal_description = models.CharField(max_length=500)

    class Meta:
        #managed = False
        db_table = 'sdg_goals'
        verbose_name_plural = 'Goals'


class Indicator(models.Model):
    id_meta_desc = models.ForeignKey('TargetDesc', models.DO_NOTHING, db_column='id_meta_desc')
    indicator_number = models.DecimalField(max_digits=65535, decimal_places=65535)
    description = models.CharField(max_length=500)
    serie_code = models.CharField(primary_key=True, max_length=50)

    class Meta:
        #managed = False
        db_table = 'sdg_indicators'
        verbose_name_plural = 'Indicators'


class IndicatorDesc(models.Model):
    id_indicator_desc = models.AutoField(primary_key=True)
    series_code = models.ForeignKey(Indicator, models.DO_NOTHING, db_column='series_code')
    reference_area_code = models.CharField(max_length=50)
    reference_area = models.CharField(max_length=100, blank=True, null=True)
    time_period = models.CharField(max_length=50)
    sex_code = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=50, blank=True, null=True)
    age_group_code = models.CharField(max_length=50)
    age_group = models.CharField(max_length=100, blank=True, null=True)
    location_code = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    unit_of_measurement_code = models.CharField(max_length=50, blank=True, null=True)
    unit_of_measurement = models.CharField(max_length=100, blank=True, null=True)
    nature_code = models.CharField(max_length=50, blank=True, null=True)
    nature = models.CharField(max_length=100, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    time_detail = models.CharField(max_length=50, blank=True, null=True)
    source_detail = models.CharField(max_length=100, blank=True, null=True)
    footnotes = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'sdg_indicators_desc'
        verbose_name = 'Indicator Description'
        verbose_name_plural = 'Indicators Descriptions'


class TargetDesc(models.Model):
    id_meta = models.ForeignKey('Target', models.DO_NOTHING, db_column='id_meta')
    id_meta_desc = models.AutoField(primary_key=True)
    meta_desc_numeber = models.DecimalField(max_digits=65535, decimal_places=65535)
    description = models.CharField(max_length=500)

    class Meta:
        #managed = False
        db_table = 'sdg_meta_desc'
        verbose_name = 'Target Description'
        verbose_name_plural = 'Targets Descriptions'


class Target(models.Model):
    id_goal = models.ForeignKey(Goal, models.DO_NOTHING, db_column='id_goal')
    id_meta = models.AutoField(primary_key=True)
    meta_number = models.DecimalField(max_digits=65535, decimal_places=65535)
    description = models.CharField(max_length=500)

    class Meta:
        #managed = False
        db_table = 'sdg_metas'
        verbose_name_plural = 'Targets'

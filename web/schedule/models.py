# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class RegSeasonSchedule2019(models.Model):
    date = models.DateField()
    away = models.CharField(max_length=30)
    home = models.CharField(max_length=30)
    scores_away = models.IntegerField()
    scores_home = models.IntegerField()

    class Meta:
        db_table = 'reg_season_schedule_2019'

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class GamePredictions2019(models.Model):
    predic_id = models.AutoField(primary_key=True)
    predic_scores_away = models.IntegerField()
    predic_scores_home = models.IntegerField()
    game = models.ForeignKey('SeasonGames2019', models.DO_NOTHING)

    class Meta:
        db_table = 'game_predictions_2019'

class SeasonGames2019(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    away = models.CharField(max_length=30)
    home = models.CharField(max_length=30)
    scores_away = models.IntegerField()
    scores_home = models.IntegerField()

    class Meta:
        db_table = 'season_games_2019'

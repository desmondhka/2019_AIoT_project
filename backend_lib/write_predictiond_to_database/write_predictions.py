import pymysql
import numpy as np
import pandas as pd

df = pd.read_csv('2019_prediction.csv')
df.head()

con = pymysql.connect('localhost',
                      'test123', 
                      'test123',
                      'projectdb')

wsql = "INSERT INTO game_predictions_2019 \
        (predic_scores_away, predic_scores_home, game_id) \
        VALUES (%s, %s, %s)"
rsql = "SELECT id FROM season_games_2019"

with con.cursor() as cursor:
    cursor.execute(rsql)
    game_ids = cursor.fetchall()
    for ids, in game_ids:
        pred = df.loc[df['game_id'] == ids]['pred_runs']
        a_pred = int(pred.iat[0])
        h_pred = int(pred.iat[1])
        #print("game={}, pred={}:{}".format(ids, a_pred, h_pred))
        
        cursor.execute(wsql, (a_pred, h_pred, ids))
        con.commit()

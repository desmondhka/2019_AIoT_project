import pymysql
import numpy as np

con = pymysql.connect('localhost', 'test123', 
    'test123', 'projectdb')

wsql = "INSERT INTO game_predictions_2019 \
        (predic_scores_away, predic_scores_home, game_id) \
        VALUES (%s, %s, %s)"
rsql = "SELECT scores_away, scores_home FROM season_games_2019"

with con.cursor() as cursor:
    cursor.execute(rsql)
    games = cursor.fetchall()
    for i in range(len(games)):
        predicA = games[i][0]+np.random.randint(-3, 4)
        predicA = 0 if predicA < 0 else predicA
        predicH = games[i][1]+np.random.randint(-3, 4)
        predicH = 0 if predicH < 0 else predicH
            
        #print("{}:{}, pred={}:{}"
        #      .format(games[i][0], games[i][1], predicA, predicH))
        
        cursor.execute(wsql, (predicA, predicH, i+1))
        con.commit()

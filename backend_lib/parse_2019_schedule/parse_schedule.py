from bs4 import BeautifulSoup
import re
import pymysql

def monthToNum(x):
    return {
        'January': '1',
        'February': '2',
        'March': '3',
        'April': '4',
        'May': '5',
        'June': '6',
        'July': '7',
        'August': '8',
        'September': '9',
        'October': '10',
        'November': '11',
        'December': '12'
    }.get(x, None)

def parseTimeString(str):
    x = str.split(', ')
    y= x[1].split()
    return x[2]+"-"+monthToNum(y[0])+"-"+y[1]

with open("MLB-schedule.shtml", "r", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp)

regularSeason = soup.find('div', 'section_content', id="div_9783493102")
gameDays = regularSeason.find_all('div')

con = pymysql.connect('localhost', 'test123', 
    'test123', 'projectdb')

with con.cursor() as cursor:
    for day in gameDays:
        if day.find(string="(Spring)") is not None:
            continue;
        date = parseTimeString(day.h3.string)
        #print(date)

        games = day.find_all('p', 'game')
        for game in games:
            match = game.find_all('a')
            away = match[0].string
            home = match[1].string

            scores = game.find_all(string=re.compile("\(\d+\)"))
            scores[0] = int(re.findall(r'\d+', scores[0])[0])
            scores[1] = int(re.findall(r'\d+', scores[1])[0])
            
            sql = "INSERT INTO season_games_2019 \
                    (date, away, home, scores_away, scores_home) \
                    VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (date, away, home, scores[0], scores[1]))
            con.commit()
            #print('\t', away, scores[0], '@', home, scores[1])
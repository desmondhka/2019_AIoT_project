from django.shortcuts import render
from django.db.models import Q
from schedule.models import SeasonGames2019 as games
from schedule.models import GamePredictions2019 as predic

# Create your views here.

def monthNameMapping(x):
	return {
		"1" : "Jan ",
		"2" : "Feb ",
		"3" : "Mar ",
		"4" : "Apr ",
		"5" : "May ",
		"6" : "Jun ",
		"7" : "Jly ",
		"8" : "Aug ",
		"9" : "Sep ",
		"10": "Nov ",
		"11": "Oct ",
		"12": "Dec "
	}.get(x, None)

def teamNameMapping(x):
	return {
		"ARI": "Arizona D'Backs",
		"ATL": "Atlanta Braves",
		"BAL": "Baltimore Orioles",
		"BOS": "Boston Red Sox",
		"CHC": "Chicago Cubs",
		"CWS": "Chicago White Sox",
		"CIN": "Cincinnati Reds",
		"CLE": "Cleveland Indians",
		"COL": "Colorado Rockies",
		"DET": "Detroit Tigers",
		"HOU": "Houston Astros",
		"KC" : "Kansas City Royals",
		"LAA": "Los Angeles Angels",
		"LAD": "Los Angeles Dodgers",
		"MIA": "Miami Marlins",
		"MIL": "Milwaukee Brewers",
		"MIN": "Minnesota Twins",
		"NYM": "New York Mets",
		"NYY": "New York Yankees",
		"OAK": "Oakland Athletics",
		"PHI": "Philadelphia Phillies",
		"PIT": "Pittsburgh Pirates",
		"SD" : "San Diego Padres",
		"SF" : "San Francisco Giants",
		"SEA": "Seattle Mariners",
		"STL": "St. Louis Cardinals",
		"TB" : "Tampa Bay Rays",
		"TEX": "Texas Rangers",
		"TOR": "Toronto Blue Jays",
		"WSH": "Washington Nationals"
	}.get(x, None)

def index(request):
	return render(request, "tables.html") #TODO: change to index.html

def showchart(request, team):
	teamFullName = teamNameMapping(team)
	deltas = [0, 0, 0, 0]
	dateList = []
	realScoreList = []
	predictScoreList =[]

	gameRecords = games.objects.\
				filter(Q(home=teamFullName) | Q(away=teamFullName))
	for record in gameRecords:
		dateList.append(monthNameMapping(str(record.date.month))+str(record.date.day))

		prediction = record.gamepredictions2019_set.get()
		if record.away == teamFullName:
			delta = abs(record.scores_away - prediction.predic_scores_away)
			realScoreList.append(record.scores_away)
			predictScoreList.append(prediction.predic_scores_away)
		elif record.home == teamFullName:
			delta = abs(record.scores_home - prediction.predic_scores_home)
			realScoreList.append(record.scores_home)
			predictScoreList.append(prediction.predic_scores_home)

		if delta == 0:
			deltas[0] += 1
		elif delta == 1:
			deltas[1] += 1
		elif delta == 2:
			deltas[2] += 1
		elif delta > 2:
			deltas[3] += 1

	return render(request, "charts.html",
			{'teamName': teamFullName,
			 'deltas': deltas,
			 'dateList': dateList,
			 'realScoreList': realScoreList,
			 'predictScoreList': predictScoreList,
			 'gameRecords': gameRecords})

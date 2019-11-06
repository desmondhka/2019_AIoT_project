from django.shortcuts import render
import os
import pandas as pd
from django.conf import settings

df = pd.read_csv(os.path.join(settings.BASE_DIR, 'df201902.csv'))

def teamNameMapping(x):
	return {
		"ARI": "Arizona D'Backs",
		"ATL": "Atlanta Braves",
		"BAL": "Baltimore Orioles",
		"BOS": "Boston Red Sox",
		"CHC": "Chicago Cubs",
		"CWS": "Chicago White Sox",
		"CHW": "Chicago White Sox",
		"CIN": "Cincinnati Reds",
		"CLE": "Cleveland Indians",
		"COL": "Colorado Rockies",
		"DET": "Detroit Tigers",
		"HOU": "Houston Astros",
		"KC" : "Kansas City Royals",
		"KCR": "Kansas City Royals",
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
		"SDP": "San Diego Padres",
		"SF" : "San Francisco Giants",
		"SFG": "San Francisco Giants",
		"SEA": "Seattle Mariners",
		"STL": "St. Louis Cardinals",
		"TB" : "Tampa Bay Rays",
		"TBR": "Tampa Bay Rays",
		"TEX": "Texas Rangers",
		"TOR": "Toronto Blue Jays",
		"WSH": "Washington Nationals",
		"WSN": "Washington Nationals"
	}.get(x, None)

# Create your views here.
def winrate(request, gameDate='2019-09-29'):
	results=[]

	gameday = df.loc[df['date']==gameDate.replace('-0', '/').replace('-', '/')]
	for i, r in gameday.iterrows():
		rowlist = []
		rowlist.append(teamNameMapping(r['team2']))
		rowlist.append(teamNameMapping(r['team1']))
		rowlist.append(r['win'])
		rowlist.append(r['pre_win'])
		rowlist.append(r['pre_probability'])
		results.append(rowlist)

	return render(request, "winrate.html",
			{'results': results, 'date': gameDate})

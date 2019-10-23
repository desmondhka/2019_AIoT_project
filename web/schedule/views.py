from django.shortcuts import render
from .models import SeasonGames2019 as games
from .models import GamePredictions2019 as predic

# Create your views here.
def showtable(request, gameDate='2019-09-29'):
	test = {'home':[], 'away':[], 'runs_away':[], 'runs_home':[],
			'predict_runs_away':[], 'predict_runs_home':[]}
	results = games.objects.filter(date=gameDate)
	for game in results:
		prediction = game.gamepredictions2019_set.get()
		test['home'].append(game.home)
		test['away'].append(game.away)
		test['runs_away'].append(game.scores_away)
		test['runs_home'].append(game.scores_home)
		test['predict_runs_away'].append(prediction.predic_scores_away)
		test['predict_runs_home'].append(prediction.predic_scores_home)

	return render(request, "tables.html",
			{'results': results, 'date': gameDate, 'range': results.count(), 'test': test})

from django.shortcuts import render
from .models import SeasonGames2019 as games
from .models import GamePredictions2019 as predic

# Create your views here.
def showtable(request, gameDate='2019-09-29'):
	results = games.objects.filter(date=gameDate)
	return render(request, "tables.html",
			{'results': results, 'date': gameDate})

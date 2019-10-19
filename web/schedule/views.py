from django.shortcuts import render
from .models import RegSeasonSchedule2019 as schedule
# Create your views here.
def showtable(request, gameDate='2019-03-28'):
	results = schedule.objects.filter(date=gameDate)
	return render(request, "tables.html",
			{'results': results, 'date': gameDate})
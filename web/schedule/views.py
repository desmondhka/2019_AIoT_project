from django.shortcuts import render

# Create your views here.
def showtable(request):
	return render(request, "tables.html")
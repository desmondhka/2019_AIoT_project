from django.urls import path
from . import views

urlpatterns = [
	path('', views.winrate, name='winrate'),
	path('<gameDate>/', views.winrate, name='winrate'),
]

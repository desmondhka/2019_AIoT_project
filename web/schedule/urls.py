from django.urls import path
from . import views

urlpatterns = [
	path('', views.showtable, name='showtable'),
    path('schedule', views.showtable, name='showtable'),
    path('schedule/<gameDate>', views.showtable, name='showtable'),
]

from django.urls import path
from . import views

urlpatterns = [
	path('', views.showtable, name='showtable'),
	path('<gameDate>/', views.showtable, name='showtable'),
]

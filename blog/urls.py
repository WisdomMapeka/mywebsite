from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:pk>/', views.first, name='first'),
	path('<int:pk>/one/', views.one, name='one'),
	path('<int:pk>/two/', views.two, name='two'),
	path('<int:pk>/three/', views.three, name='three'),
	path('<int:pk>/four/', views.four, name='four'),
	path('<int:pk>/five/', views.five, name='five'),
	path('<int:pk>/six/', views.six, name='six'),
	] 

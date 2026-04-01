from django.urls import path
from . import views

app_name = 'cards'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_word, name='add_word'),
    path('learn/', views.learn, name='learn'),
    path('api/random/', views.get_random_word, name='get_random_word'),
    path('word/<int:word_id>/', views.get_word, name='get_word'),
]

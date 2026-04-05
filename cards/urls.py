from django.urls import path
from . import views

app_name = 'cards'

urlpatterns = [
    path('', views.home, name='home'),
    path('set/add/', views.add_word_set, name='add_word_set'),
    path('set/<int:set_id>/', views.word_set_detail, name='word_set_detail'),
    path('set/<int:set_id>/learn/', views.learn_set, name='learn_set'),
    path('set/<int:set_id>/api/random/', views.get_random_word, name='get_random_word_set'),
    path('word/<int:word_id>/learned/', views.mark_word_learned, name='mark_word_learned'),
    # Legacy URLs (redirect to home)
    path('add/', views.add_word, name='add_word'),
    path('learn/', views.learn, name='learn'),
    path('api/random/', views.get_random_word, name='get_random_word'),
    path('word/<int:word_id>/', views.get_word, name='get_word'),
]

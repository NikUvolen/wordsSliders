from django.urls import path

from .views import MainView, WordsSetsView

urlpatterns = [
    path('/test', MainView.as_view(), name='main_page'),
    path('', WordsSetsView.as_view(), name='words_sets')
]

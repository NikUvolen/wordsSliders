from django.shortcuts import render
from django import views

from .models import WordsSet


class MainView(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'a_sliders/index.html')
    
class WordsSetsView(views.View):
    def get(self, request, *args, **kwargs):
        words_sets = WordsSet.objects.all()
        context = {
            'words_sets': words_sets
        }
        return render(request, 'a_sliders/words_sets.html', context=context)

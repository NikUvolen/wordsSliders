from django.shortcuts import render
from django import views

from .models import WordsSet

    
class WordsSetsView(views.View):
    def get(self, request, *args, **kwargs):
        words_sets = WordsSet.objects.select_related('creator').all()
        context = {
            'words_sets': words_sets
        }
        return render(request, 'a_sliders/words_sets.html', context=context)
    

class WordSliderView(views.View):
    def get(self, request, user_id, words_slides_slug, *args, **kwargs):
        return render(request, 'a_sliders/index.html')

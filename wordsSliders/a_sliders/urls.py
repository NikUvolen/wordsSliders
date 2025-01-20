from django.urls import path

from .views import WordsSetsView, WordSliderView

urlpatterns = [
    path('', WordsSetsView.as_view(), name='words_sets'),
    path('words-slides/<int:user_id>-<str:words_slides_slug>', WordSliderView.as_view(), name='word_slider_view'),
]

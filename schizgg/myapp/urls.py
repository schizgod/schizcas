from django.urls import path
from .views import home, casino, blackjack_helper, contacts, article_detail, blackjack_publication_detail

urlpatterns = [
    path('', home, name='home'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
    path('casino/', casino, name='casino'),
    path('blackjack/', blackjack_helper, name='blackjack_helper'),
    path('contacts/', contacts, name='contacts'),
    path('blackjack/<int:pk>/', blackjack_publication_detail, name='blackjack_publication_detail'),
]

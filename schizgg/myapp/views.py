from django.shortcuts import render, get_object_or_404
from .models import Article, CasinoBanner, BlackjackPublication

def home(request):
    articles = Article.objects.all()  # Получаем все статьи
    return render(request, 'myapp/home.html', {'articles': articles})

def casino(request):
    casino_banners = CasinoBanner.objects.all()
    return render(request, 'myapp/casino.html', {'casino_banners': casino_banners})

def blackjack_helper(request):
    blackjack_publications = BlackjackPublication.objects.all()
    return render(request, 'myapp/blackjack_helper.html', {'blackjack_publications': blackjack_publications})

def blackjack_publication_detail(request, pk):
    blackjack_publication = get_object_or_404(BlackjackPublication, pk=pk)
    return render(request, 'myapp/blackjack_publication_detail.html', {'blackjack_publication': blackjack_publication})

def contacts(request):
    return render(request, 'myapp/contacts.html')

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'myapp/article_detail.html', {'article': article})

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import random
from .models import Word

def home(request):
    """Main page with all words and learning interface"""
    words = Word.objects.all()
    context = {
        'words': words,
        'total_words': words.count()
    }
    return render(request, 'cards/home.html', context)

def add_word(request):
    """Add a new word"""
    if request.method == 'POST':
        en = request.POST.get('en', '').strip()
        ru = request.POST.get('ru', '').strip()
        
        if en and ru:
            Word.objects.create(en=en, ru=ru)
            return redirect('cards:home')
    
    return render(request, 'cards/add_word.html')

def learn(request):
    """Learning mode with random words"""
    words = list(Word.objects.all())
    
    if not words:
        return redirect('cards:add_word')
    
    # Get random word
    current_word = random.choice(words)
    
    context = {
        'word': current_word,
        'total_words': len(words),
        'show_translation': False,
    }
    return render(request, 'cards/learn.html', context)

@require_http_methods(["GET"])
def get_random_word(request):
    """Get a random word (JSON)"""
    words = Word.objects.all()
    
    if not words.exists():
        return JsonResponse({'error': 'No words available'}, status=404)
    
    word = random.choice(list(words))
    return JsonResponse({
        'id': word.id,
        'en': word.en,
        'ru': word.ru
    })

@require_http_methods(["GET"])
def get_word(request, word_id):
    """Get a specific word (JSON)"""
    word = get_object_or_404(Word, id=word_id)
    return JsonResponse({
        'id': word.id,
        'en': word.en,
        'ru': word.ru
    })

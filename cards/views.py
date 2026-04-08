from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import random
from .models import Word, WordSet

def home(request):
    """Main page with word sets"""
    word_sets = WordSet.objects.all()
    context = {
        'word_sets': word_sets,
    }
    return render(request, 'cards/home.html', context)

def word_set_detail(request, set_id):
    """Word set detail page with editing capabilities"""
    word_set = get_object_or_404(WordSet, id=set_id)
    words = word_set.words.filter(is_learned=False)
    
    if request.method == 'POST':
        # Обработка добавления нового слова
        if 'add_word' in request.POST:
            en = request.POST.get('en', '').strip()
            ru = request.POST.get('ru', '').strip()
            if en and ru:
                Word.objects.create(word_set=word_set, en=en, ru=ru)
                return redirect('cards:word_set_detail', set_id=set_id)
        
        # Обработка изменения названия набора
        elif 'update_set_name' in request.POST:
            new_name = request.POST.get('set_name', '').strip()
            if new_name:
                word_set.name = new_name
                word_set.save()
                return redirect('cards:word_set_detail', set_id=set_id)
        
        # Обработка обновления слов
        elif 'update_words' in request.POST:
            # Обновляем существующие слова (только если поля были отправлены)
            for word in words:
                en_key = f'en_{word.id}'
                ru_key = f'ru_{word.id}'
                if en_key in request.POST and ru_key in request.POST:
                    en = request.POST.get(en_key, '').strip()
                    ru = request.POST.get(ru_key, '').strip()
                    if en and ru:
                        word.en = en
                        word.ru = ru
                        word.save()
            
            # Всегда проверяем, есть ли слова для изучения после любых изменений
            learnable_words = word_set.words.filter(is_learned=False)
            if learnable_words.exists():
                # Перенаправляем на страницу обучения
                return redirect('cards:learn_set', set_id=set_id)
            else:
                # Если нет слов для изучения, остаемся на странице
                pass
    
    # Проверяем, есть ли слова для изучения
    learnable_words = word_set.words.filter(is_learned=False)
    
    context = {
        'word_set': word_set,
        'words': words,
        'can_start_learning': learnable_words.exists(),
    }
    return render(request, 'cards/word_set_detail.html', context)

def learn_set(request, set_id):
    """Learning mode for a specific word set"""
    word_set = get_object_or_404(WordSet, id=set_id)
    all_words = word_set.words.all()
    words = list(all_words.filter(is_learned=False))
    
    if not words:
        return redirect('cards:word_set_detail', set_id=set_id)
    
    # Get random word
    current_word = random.choice(words)
    learned_words = all_words.filter(is_learned=True).count()
    total_words = all_words.count()
    progress_percentage = int((learned_words / total_words) * 100) if total_words else 0
    
    context = {
        'word': current_word,
        'word_set': word_set,
        'total_words': total_words,
        'learned_words': learned_words,
        'remaining_words': len(words),
        'progress_percentage': progress_percentage,
        'show_translation': False,
    }
    return render(request, 'cards/learn.html', context)

def add_word_set(request):
    """Create a new word set"""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            word_set = WordSet.objects.create(name=name)
            return redirect('cards:word_set_detail', set_id=word_set.id)
    
    return render(request, 'cards/add_word_set.html')

def add_word(request):
    """Add a new word (legacy, redirect to home)"""
    return redirect('cards:home')

def learn(request):
    """Learning mode (legacy, redirect to home)"""
    return redirect('cards:home')

@require_http_methods(["GET"])
def get_random_word(request, set_id=None):
    """Get a random word (JSON)"""
    if set_id:
        word_set = get_object_or_404(WordSet, id=set_id)
        words = word_set.words.filter(is_learned=False)
    else:
        words = Word.objects.filter(is_learned=False)
    
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

@require_http_methods(["POST"])
def mark_word_learned(request, word_id):
    """Mark a word as learned so it is skipped during learning."""
    word = get_object_or_404(Word, id=word_id)
    word.is_learned = True
    word.save()

    next_url = request.POST.get('next') or request.POST.get('return_url')
    if next_url:
        return redirect(next_url)

    return JsonResponse({
        'success': True,
        'message': f'Слово "{word.en}" выучено!'
    })

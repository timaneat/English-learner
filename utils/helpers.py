"""
Helper utilities for the English Learner app
"""

def format_progress(current, total):
    """Format progress string"""
    return f"Слово {current + 1} из {total}"

def calculate_progress_percentage(current, total):
    """Calculate progress percentage"""
    if total == 0:
        return 0
    return (current + 1) / total

def validate_word_input(en_word, ru_word):
    """Validate word input"""
    return bool(en_word.strip() and ru_word.strip())
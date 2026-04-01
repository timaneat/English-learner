"""
Configuration settings for the English Learner app
"""

# App configuration
APP_TITLE = "My English Cards"
APP_ICON = "🇬🇧"

# Default words for initial setup
DEFAULT_WORDS = [
    {"en": "Hello", "ru": "Привет"},
    {"en": "Success", "ru": "Успех"},
    {"en": "World", "ru": "Мир"}
]

# Session state keys
SESSION_WORDS_KEY = 'my_words'
SESSION_INDEX_KEY = 'idx'
SESSION_FLIPPED_KEY = 'flipped'
"""
Data management for words dictionary
"""
import streamlit as st
from config import SESSION_WORDS_KEY, SESSION_INDEX_KEY, SESSION_FLIPPED_KEY, DEFAULT_WORDS


def initialize_session_state():
    """Initialize session state with default values"""
    if SESSION_WORDS_KEY not in st.session_state:
        st.session_state[SESSION_WORDS_KEY] = DEFAULT_WORDS.copy()

    if SESSION_INDEX_KEY not in st.session_state:
        st.session_state[SESSION_INDEX_KEY] = 0

    if SESSION_FLIPPED_KEY not in st.session_state:
        st.session_state[SESSION_FLIPPED_KEY] = False


def get_words():
    """Get all words from session state"""
    return st.session_state[SESSION_WORDS_KEY]


def add_word(en_word, ru_word):
    """Add a new word to the dictionary"""
    if en_word and ru_word:
        st.session_state[SESSION_WORDS_KEY].append({"en": en_word, "ru": ru_word})
        return True
    return False


def get_current_word():
    """Get the currently displayed word"""
    words = get_words()
    if words:
        return words[st.session_state[SESSION_INDEX_KEY]]
    return None


def get_current_index():
    """Get current word index"""
    return st.session_state[SESSION_INDEX_KEY]


def get_total_words():
    """Get total number of words"""
    return len(get_words())


def next_word():
    """Move to next word"""
    words = get_words()
    if words:
        st.session_state[SESSION_INDEX_KEY] = (st.session_state[SESSION_INDEX_KEY] + 1) % len(words)
        st.session_state[SESSION_FLIPPED_KEY] = False


def previous_word():
    """Move to previous word"""
    words = get_words()
    if words:
        st.session_state[SESSION_INDEX_KEY] = (st.session_state[SESSION_INDEX_KEY] - 1) % len(words)
        st.session_state[SESSION_FLIPPED_KEY] = False


def flip_card():
    """Flip the current card"""
    st.session_state[SESSION_FLIPPED_KEY] = not st.session_state[SESSION_FLIPPED_KEY]


def is_flipped():
    """Check if card is flipped"""
    return st.session_state[SESSION_FLIPPED_KEY]


def clear_all_words():
    """Clear all words (for testing)"""
    st.session_state[SESSION_WORDS_KEY] = []
    st.session_state[SESSION_INDEX_KEY] = 0
    st.session_state[SESSION_FLIPPED_KEY] = False
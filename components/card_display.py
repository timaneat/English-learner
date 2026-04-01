"""
Card display component
"""
import streamlit as st
from data.words_manager import get_current_word, is_flipped, flip_card, next_word, previous_word, get_current_index, get_total_words


def render_card_display():
    """Render the main card display area"""
    words = get_current_word()

    if not words:
        st.info("Словарь пуст. Добавь слова в боковом меню!")
        return

    # Determine what to display
    display_text = words['ru'] if is_flipped() else words['en']
    label = "🇷🇺 Перевод" if is_flipped() else "🇬🇧 Оригинал"

    st.caption(label)
    st.markdown(f'<div class="card-box">{display_text}</div>', unsafe_allow_html=True)

    # Control buttons
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if st.button("🔄 Перевернуть"):
            flip_card()
            st.rerun()

    with col3:
        if st.button("Next ➡️"):
            next_word()
            st.rerun()

    with col1:
        if st.button("⬅️ Back"):
            previous_word()
            st.rerun()

    # Progress
    current_idx = get_current_index()
    total_words = get_total_words()
    st.write(f"Слово {current_idx + 1} из {total_words}")
    st.progress((current_idx + 1) / total_words)
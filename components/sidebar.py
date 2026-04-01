"""
Sidebar component for adding words
"""
import streamlit as st
from data.words_manager import add_word, clear_all_words


def render_sidebar():
    """Render the sidebar with word addition functionality"""
    with st.sidebar:
        st.header("➕ Добавить слово")

        new_en = st.text_input("Слово на английском")
        new_ru = st.text_input("Перевод")

        if st.button("Сохранить в словарь"):
            if add_word(new_en, new_ru):
                st.success(f"Добавлено: {new_en}")
            else:
                st.error("Заполни оба поля!")

        # Clear button for testing
        if st.button("🗑 Очистить всё"):
            clear_all_words()
            st.rerun()
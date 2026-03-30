import streamlit as st

# 1. Настройка внешнего вида (как в твоем дизайне Figma)
st.set_page_config(page_title="My English Cards", page_icon="🇬🇧")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3em; background-color: #4A90E2; color: white; }
    .card-box {
        padding: 60px 20px;
        border-radius: 25px;
        background: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border: 2px solid #e0e0e0;
        margin: 20px 0;
        font-size: 32px;
        font-weight: bold;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Инициализация базы слов в памяти приложения
if 'my_words' not in st.session_state:
    st.session_state.my_words = [
        {"en": "Hello", "ru": "Привет"},
        {"en": "Success", "ru": "Успех"}
    ]
if 'idx' not in st.session_state: st.session_state.idx = 0
if 'flipped' not in st.session_state: st.session_state.flipped = False

# --- БОКОВАЯ ПАНЕЛЬ (Добавление слов) ---
with st.sidebar:
    st.header("➕ Добавить слово")
    new_en = st.text_input("Слово на английском")
    new_ru = st.text_input("Перевод")
    if st.button("Сохранить в словарь"):
        if new_en and new_ru:
            st.session_state.my_words.append({"en": new_en, "ru": new_ru})
            st.success(f"Добавлено: {new_en}")
        else:
            st.error("Заполни оба поля!")

# --- ОСНОВНОЙ ЭКРАН (Тренажер) ---
st.title("🗂 Мои карточки")

if len(st.session_state.my_words) > 0:
    current_card = st.session_state.my_words[st.session_state.idx]
    
    # Логика отображения (лицевая или обратная сторона)
    display_text = current_card['ru'] if st.session_state.flipped else current_card['en']
    label = "🇷🇺 Перевод" if st.session_state.flipped else "🇬🇧 Оригинал"
    
    st.caption(label)
    st.markdown(f'<div class="card-box">{display_text}</div>', unsafe_allow_html=True)

    # Кнопки управления
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🔄 Перевернуть"):
            st.session_state.flipped = not st.session_state.flipped
            st.rerun()
            
    with col3:
        if st.button("Next ➡️"):
            st.session_state.idx = (st.session_state.idx + 1) % len(st.session_state.my_words)
            st.session_state.flipped = False
            st.rerun()
            
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.idx = (st.session_state.idx - 1) % len(st.session_state.my_words)
            st.session_state.flipped = False
            st.rerun()

    # Прогресс
    st.write(f"Слово {st.session_state.idx + 1} из {len(st.session_state.my_words)}")
    st.progress((st.session_state.idx + 1) / len(st.session_state.my_words))

else:
    st.info("Словарь пуст. Добавь слова в боковом меню!")

# Кнопка очистки (для тестов)
if st.sidebar.button("🗑 Очистить всё"):
    st.session_state.my_words = []
    st.session_state.idx = 0
    st.rerun()
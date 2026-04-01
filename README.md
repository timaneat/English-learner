# English Learner App

Приложение для изучения английских слов с интерактивными карточками.

## 🚀 Развертывание в интернете

### Вариант 1: Streamlit Cloud (Рекомендую! Бесплатно)

#### Шаг 1: Подготовка
1. Убедитесь, что у вас есть аккаунт на [GitHub](https://github.com)
2. Репозиторий уже готов: `timaneat/English-learner`

#### Шаг 2: Развертывание
1. Перейдите на [share.streamlit.io](https://share.streamlit.io)
2. Авторизуйтесь через GitHub
3. Выберите репозиторий `timaneat/English-learner`
4. Укажите главный файл: `streamlit_app.py`
5. В разделе "Advanced settings" укажите:
   - Requirements file: `requirements_streamlit.txt`
6. Нажмите "Deploy!"

#### Шаг 3: Готово!
Ваше приложение будет доступно по публичному URL вида:
`https://english-learner.streamlit.app`

### Вариант 2: Django на Heroku (Бесплатный тариф)

#### Шаг 1: Установка Heroku CLI
```bash
# macOS
brew install heroku/brew/heroku

# Или скачайте с https://devcenter.heroku.com/articles/heroku-cli
```

#### Шаг 2: Подготовка проекта
```bash
# Войдите в Heroku
heroku login

# Создайте приложение
heroku create your-english-cards-app

# Добавьте PostgreSQL (бесплатно)
heroku addons:create heroku-postgresql:hobby-dev

# Загрузите код
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

#### Шаг 3: Настройка базы данных
```bash
# Откройте Heroku dashboard и настройте переменные окружения
# Или через CLI:
heroku config:set DJANGO_SETTINGS_MODULE=english_learner.settings
```

### Вариант 3: Railway (Очень просто)

1. Перейдите на [railway.app](https://railway.app)
2. Авторизуйтесь через GitHub
3. Выберите репозиторий `timaneat/English-learner`
4. Railway автоматически определит Django проект
5. Нажмите "Deploy" - готово!

### Вариант 4: Render (Бесплатно)

1. Перейдите на [render.com](https://render.com)
2. Авторизуйтесь через GitHub
3. Создайте "Web Service"
4. Выберите репозиторий `timaneat/English-learner`
5. Настройте:
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn english_learner.wsgi:application --bind 0.0.0.0:$PORT`

## 📁 Структура проекта

```
English-learner/
├── streamlit_app.py              # Streamlit версия
├── requirements_streamlit.txt    # Зависимости для Streamlit
├── requirements.txt              # Зависимости для Django
├── .streamlit/config.toml        # Конфигурация Streamlit
├── cards/                        # Django приложение
├── english_learner/              # Django настройки
├── manage.py                    # Django менеджер
├── Procfile                     # Для Heroku
├── runtime.txt                  # Python версия для Heroku
└── README.md                    # Этот файл
```

## 🎯 Функциональность

### Streamlit версия:
- ✅ Добавление новых слов
- ✅ Интерактивные карточки
- ✅ Переворот карточек
- ✅ Современный дизайн
- ❌ Данные теряются при перезагрузке

### Django версия:
- ✅ Добавление новых слов
- ✅ Интерактивные карточки
- ✅ Переворот карточек
- ✅ Красивый дизайн
- ✅ Постоянное хранение данных
- ✅ 20 предустановленных слов

## 🔧 Локальный запуск

### Streamlit версия:
```bash
pip install -r requirements_streamlit.txt
streamlit run streamlit_app.py
```

### Django версия:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata cards/fixtures/initial_words.json
python manage.py runserver
```

## 📊 Сравнение платформ

| Платформа | Цена | Сложность | База данных | Рекомендация |
|-----------|------|-----------|-------------|--------------|
| Streamlit Cloud | Бесплатно | Очень просто | Нет | ⭐ Для быстрого старта |
| Railway | Бесплатно | Просто | PostgreSQL | ⭐ Для Django |
| Render | Бесплатно | Средне | PostgreSQL | Хороший выбор |
| Heroku | Бесплатно | Сложно | PostgreSQL | Для продвинутых |

## 🤝 Вклад в проект

Приветствуются любые улучшения и предложения!

---

**Автор:** timaneat
**Дата:** 2026

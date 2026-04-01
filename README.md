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

### Вариант 3: Render (Бесплатно - УПРОЩЕННАЯ ИНСТРУКЦИЯ)

#### 🎯 Почему Render?
- **750 бесплатных часов** в месяц (примерно 31 день)
- **PostgreSQL база данных** включена
- **Автоматические SSL сертификаты**
- **Глобальная CDN** для быстрой загрузки
- **Интеграция с GitHub** - автообновление при push

#### 📋 Быстрая инструкция (если стандартная не работает):

##### Шаг 1: Регистрация
**[render.com](https://render.com)** → Зарегистрироваться

##### Шаг 2: Создать Web Service
"New +" → "Web Service" → "Connect GitHub" → Выбрать `timaneat/English-learner`

##### Шаг 3: Настройки (УПРОЩЕННЫЕ)
```
Name: english-cards
Environment: Python 3
Build Command: ./build_simple.sh
Start Command: gunicorn english_learner.wsgi:application --bind 0.0.0.0:$PORT
```

##### Шаг 4: Переменные окружения
```
DJANGO_SETTINGS_MODULE = english_learner.settings
DEBUG = False
SECRET_KEY = django-insecure-any-random-string-here
```

##### Шаг 5: База данных
"New +" → "PostgreSQL" → Создать → Скопировать DATABASE_URL

##### Шаг 6: Развертывание
"Create Web Service" → Ждать 5-10 минут → Готово!

#### 🚨 Если возникают ошибки:
1. **Проверьте [TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - подробные решения
2. **Используйте Railway** - проще чем Render
3. **Попробуйте Streamlit Cloud** - самый простой вариант

#### 🔧 Альтернативные команды сборки:
- **Простая:** `./build_simple.sh`
- **Полная:** `./build.sh`
- **Docker:** Используйте Dockerfile

#### 🎯 Что делать после развертывания:
1. Открыть URL и проверить работу
2. Добавить слова через интерфейс
3. Протестировать режим обучения
4. Поделиться ссылкой!

**❌ Возникают ошибки?** Сначала посмотрите [TROUBLESHOOTING.md](TROUBLESHOOTING.md)!

**Готовы начать?** Перейдите на [render.com](https://render.com)! 🚀

## 📁 Структура проекта

```
English-learner/
├── streamlit_app.py              # Streamlit версия приложения
├── requirements_streamlit.txt    # Зависимости для Streamlit
├── requirements.txt              # Зависимости для Django
├── .streamlit/config.toml        # Конфигурация Streamlit
├── cards/                        # Django приложение
│   ├── models.py                 # Модель Word
│   ├── views.py                  # Представления (home, learn, add_word)
│   ├── urls.py                   # Маршруты приложения
│   ├── templates/cards/          # HTML шаблоны
│   │   ├── home.html            # Главная страница
│   │   ├── learn.html           # Страница обучения
│   │   └── add_word.html        # Добавление слов
│   └── static/cards/            # Статические файлы
├── english_learner/              # Django настройки проекта
│   ├── settings.py              # Основные настройки
│   ├── urls.py                  # Главные маршруты
│   └── wsgi.py                  # WSGI конфигурация
├── manage.py                    # Django менеджер команд
├── build.sh                     # Скрипт сборки для развертывания
├── build_simple.sh              # Упрощенный скрипт сборки
├── Dockerfile                   # Docker конфигурация
├── render_settings.py           # Настройки для Render
├── TROUBLESHOOTING.md           # Руководство по устранению ошибок
├── Procfile                     # Для Heroku
├── runtime.txt                  # Python версия для Heroku
└── README.md                    # Этот файл
```

## 🖥️ Локальный запуск

### Streamlit версия:
```bash
pip install -r requirements_streamlit.txt
streamlit run streamlit_app.py
```

### Django версия:
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata words
python manage.py runserver
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
| **Streamlit Cloud** | 🟢 Бесплатно | 🟢 Очень просто | 🔴 Нет | ⭐ Для быстрого старта |
| **Railway** | 🟢 Бесплатно | 🟢 Просто | 🟢 PostgreSQL | ⭐ Для Django |
| **Render** | 🟢 Бесплатно | 🟡 Средне | 🟢 PostgreSQL | ⭐ Подробная инструкция |
| **Heroku** | 🟢 Бесплатно | 🔴 Сложно | 🟢 PostgreSQL | Для продвинутых |

## 🤝 Вклад в проект

Приветствуются любые улучшения и предложения!

### Как внести вклад:
1. Fork репозиторий
2. Создайте feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit изменения (`git commit -m 'Add some AmazingFeature'`)
4. Push в branch (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

### Идеи для улучшений:
- ✅ Добавление категорий слов (животные, еда, путешествия)
- ✅ Система прогресса и статистики
- ✅ Тесты на знание слов
- ✅ Темная тема интерфейса
- ✅ Экспорт/импорт словаря
- ✅ Мобильное приложение

## 📞 Контакты

- **GitHub:** [timaneat](https://github.com/timaneat)
- **Email:** [Ваш email]
- **Telegram:** [Ваш Telegram]

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. Подробности в файле `LICENSE`.

---

**🚀 Удачи в изучении английского!**  
**Made with ❤️ by timaneat**

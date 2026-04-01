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

### Вариант 3: Render (Бесплатно - ПОДРОБНАЯ ИНСТРУКЦИЯ)

#### 🎯 Почему Render?
- **750 бесплатных часов** в месяц (примерно 31 день)
- **PostgreSQL база данных** включена
- **Автоматические SSL сертификаты**
- **Глобальная CDN** для быстрой загрузки
- **Интеграция с GitHub** - автообновление при push

#### 📋 Пошаговая инструкция:

##### Шаг 1: Регистрация
1. Перейдите на **[render.com](https://render.com)**
2. Зарегистрируйтесь (можно через GitHub аккаунт)
3. Подтвердите email

##### Шаг 2: Создание Web Service
1. Нажмите **"New +"** → **"Web Service"**
2. Выберите **"Connect GitHub"**
3. Авторизуйте Render для доступа к репозиториям
4. Найдите и выберите `timaneat/English-learner`

##### Шаг 3: Настройка сервиса
Заполните поля:

```
Name: english-cards (или любое имя)
Environment: Python 3
Region: Frankfurt (EU Central) - ближе к России
Branch: main (или ваша ветка)
```

##### Шаг 4: Настройка Build & Start
```
Build Command: ./build.sh
Start Command: gunicorn english_learner.wsgi:application --bind 0.0.0.0:$PORT
```

##### Шаг 5: Переменные окружения
Нажмите **"Advanced"** и добавьте:

```
DJANGO_SETTINGS_MODULE = english_learner.settings
DEBUG = False
SECRET_KEY = ваш-секретный-ключ (придумайте сложный)
```

##### Шаг 6: Создание базы данных
1. Нажмите **"New +"** → **"PostgreSQL"**
2. Name: `english-cards-db`
3. Database: `english_cards`
4. Username: `english_cards_user`
5. Нажмите **"Create Database"**

##### Шаг 7: Подключение БД к приложению
1. Перейдите в настройки вашего Web Service
2. В разделе **"Environment"** добавьте:
```
DATABASE_URL = postgresql://[ваши-данные-из-PostgreSQL]
```
(Скопируйте DATABASE_URL из настроек PostgreSQL)

##### Шаг 8: Развертывание
1. Нажмите **"Create Web Service"**
2. Ждите 5-10 минут пока соберется и запустится
3. Готово! Получите URL вида: `https://english-cards.onrender.com`

#### 🔧 Возможные проблемы и решения:

##### Ошибка "ModuleNotFoundError"
- Проверьте что все пакеты в `requirements.txt`
- Убедитесь что `build.sh` исполняемый

##### Ошибка базы данных
- Проверьте `DATABASE_URL` в переменных окружения
- Убедитесь что PostgreSQL создана и подключена

##### Сайт не загружается
- Проверьте логи в Render dashboard
- Возможно нужно подождать 5-10 минут после создания

##### Статические файлы не работают
- WhiteNoise должен автоматически настроиться через `build.sh`

#### 💰 Тарифы Render:
- **Free**: 750 часов/месяц, 1GB RAM, 1GB disk
- **Starter**: $7/месяц - для постоянного использования
- **Pro**: От $25/месяц - для серьезных проектов

#### ⚡ Преимущества Render:
- ✅ Бесплатный тариф подходит для тестирования
- ✅ PostgreSQL включена (не нужно платить отдельно)
- ✅ Автоматические обновления при push в GitHub
- ✅ SSL сертификаты
- ✅ Хорошая производительность
- ✅ Русскоязычная поддержка

#### 🚨 Важные замечания:
- **Free тариф "засыпает"** после 15 минут без активности
- Первый запрос может быть медленным (15-30 сек)
- Ограничение по трафику и ресурсам
- Для продакшена лучше платный тариф

#### 🎯 Что делать после развертывания:
1. Откройте URL и проверьте работу
2. Добавьте несколько слов
3. Протестируйте режим обучения
4. Поделитесь ссылкой с друзьями!

**Готовы начать?** Перейдите на [render.com](https://render.com) и следуйте инструкциям выше! 🚀

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
| **Streamlit Cloud** | 🟢 Бесплатно | 🟢 Очень просто | 🔴 Нет | ⭐ Для быстрого старта |
| **Railway** | 🟢 Бесплатно | 🟢 Просто | 🟢 PostgreSQL | ⭐ Для Django |
| **Render** | 🟢 Бесплатно | 🟡 Средне | 🟢 PostgreSQL | ⭐ Подробная инструкция |
| **Heroku** | 🟢 Бесплатно | 🔴 Сложно | 🟢 PostgreSQL | Для продвинутых |

## 🤝 Вклад в проект

Приветствуются любые улучшения и предложения!

---

**Автор:** timaneat
**Дата:** 2026

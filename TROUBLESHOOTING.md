# 🚨 TROUBLESHOOTING GUIDE для Render

## 🔍 Распространенные ошибки и решения

### ❌ "Build failed" на этапе установки зависимостей

**Симптомы:**
```
ERROR: Could not find a version that satisfies the requirement Django==6.0.3
```

**Решения:**
1. **Используйте более старую версию Python:**
   - В настройках Render измените Environment на `Python 3.11`
   - Или обновите `runtime.txt` на `python-3.11.0`

2. **Упростите requirements.txt:**
```txt
Django==5.0.6
gunicorn==21.2.0
whitenoise==6.6.0
dj-database-url==2.1.0
psycopg2-binary==2.9.7
```

### ❌ "ModuleNotFoundError" при запуске

**Симптомы:**
```
ModuleNotFoundError: No module named 'django'
```

**Решения:**
1. **Проверьте build.sh:**
```bash
#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt
```

2. **Используйте build_simple.sh:**
   - Измените Build Command на `./build_simple.sh`

### ❌ Ошибка базы данных

**Симптомы:**
```
django.db.utils.OperationalError: could not connect to server
```

**Решения:**
1. **Проверьте DATABASE_URL:**
   - В Environment variables добавьте:
   ```
   DATABASE_URL = [скопируйте из PostgreSQL настроек]
   ```

2. **Создайте новую базу данных:**
   - Удалите старую PostgreSQL
   - Создайте новую с простым именем

### ❌ "Static files not found"

**Симптомы:**
CSS/JS файлы не загружаются

**Решения:**
1. **Проверьте WhiteNoise:**
   - Убедитесь что `whitenoise` в requirements.txt
   - Проверьте что middleware настроен правильно

2. **Запустите collectstatic:**
```bash
python manage.py collectstatic --no-input --clear
```

### ❌ "Application failed to respond"

**Симптомы:**
Сервер не отвечает на запросы

**Решения:**
1. **Проверьте логи Render:**
   - В dashboard Render нажмите на сервис
   - Посмотрите вкладку "Logs"

2. **Простой тест:**
   - Измените Start Command на:
   ```
   python manage.py runserver 0.0.0.0:$PORT
   ```

### ❌ "Timeout during build"

**Симптомы:**
Сборка прерывается по таймауту

**Решения:**
1. **Упростите build.sh:**
   - Удалите необязательные команды
   - Используйте `build_simple.sh`

2. **Проверьте зависимости:**
   - Удалите тяжелые пакеты
   - Используйте `--no-cache-dir`

## 🛠️ АЛЬТЕРНАТИВНЫЕ РЕШЕНИЯ

### Вариант 1: Использовать Railway вместо Render
Railway проще в настройке и тоже бесплатный.

### Вариант 2: Использовать Streamlit Cloud
Если не нужна база данных - самый простой вариант.

### Вариант 3: Локальное развертывание
```bash
# На своем сервере
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
```

## 📞 ПОЛУЧЕНИЕ ПОМОЩИ

1. **Проверьте логи Render** - там подробная информация об ошибках
2. **Протестируйте локально:**
```bash
./test_deployment.sh
```
3. **Проверьте версию Python** в runtime.txt
4. **Упростите настройки** - начните с минимального requirements.txt

## 🔧 БЫСТРЫЕ ИСПРАВЛЕНИЯ

### Минимальный requirements.txt:
```txt
Django==5.0.6
gunicorn==21.2.0
whitenoise==6.6.0
```

### Минимальный build.sh:
```bash
#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

### Минимальные Environment Variables:
```
DJANGO_SETTINGS_MODULE = english_learner.settings
DEBUG = False
SECRET_KEY = any-random-string-here
```

## 📋 ЧЕКЛИСТ ПЕРЕД РАЗВЕРТЫВАНИЕМ

- [ ] Репозиторий публичный на GitHub
- [ ] requirements.txt содержит только необходимые пакеты
- [ ] build.sh/executable и простой
- [ ] runtime.txt указывает правильную версию Python
- [ ] Environment variables настроены
- [ ] PostgreSQL создана и подключена
- [ ] Локально работает: `./test_deployment.sh`

---
*Если ничего не помогает - попробуйте Railway или Streamlit Cloud!* 🚀
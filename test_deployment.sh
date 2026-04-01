#!/bin/bash

echo "🧪 Тестирование English Learner перед развертыванием"
echo "=================================================="

# Проверка Python
echo "🐍 Проверка Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 не найден"
    exit 1
fi
echo "✅ Python3 найден: $(python3 --version)"

# Проверка виртуального окружения
echo ""
echo "🔧 Проверка виртуального окружения..."
if [ ! -d "venv" ]; then
    echo "❌ Виртуальное окружение не найдено"
    echo "Создайте: python3 -m venv venv"
    exit 1
fi
echo "✅ Виртуальное окружение найдено"

# Активация venv и проверка зависимостей
echo ""
echo "📦 Проверка зависимостей..."
source venv/bin/activate
if ! python -c "import django" &> /dev/null; then
    echo "❌ Django не установлен"
    echo "Установите: pip install -r requirements.txt"
    exit 1
fi
echo "✅ Django установлен: $(python -c "import django; print(django.VERSION)")"

# Проверка миграций
echo ""
echo "🗄️  Проверка базы данных..."
python manage.py check
if [ $? -ne 0 ]; then
    echo "❌ Ошибки в настройках Django"
    exit 1
fi
echo "✅ Настройки Django корректны"

# Проверка статических файлов
echo ""
echo "🎨 Проверка статических файлов..."
python manage.py collectstatic --no-input --dry-run
if [ $? -ne 0 ]; then
    echo "❌ Проблемы со статическими файлами"
    exit 1
fi
echo "✅ Статические файлы готовы"

# Тестовый запуск
echo ""
echo "🚀 Тестовый запуск сервера..."
timeout 5 python manage.py runserver 0.0.0.0:8000 &
SERVER_PID=$!
sleep 3

if kill -0 $SERVER_PID 2>/dev/null; then
    echo "✅ Сервер запустился успешно"
    kill $SERVER_PID
else
    echo "❌ Сервер не запустился"
    exit 1
fi

echo ""
echo "🎉 Все проверки пройдены!"
echo "================================"
echo "✅ Python3: OK"
echo "✅ Виртуальное окружение: OK"
echo "✅ Django: OK"
echo "✅ Настройки: OK"
echo "✅ Статические файлы: OK"
echo "✅ Сервер: OK"
echo ""
echo "🚀 Готово к развертыванию на Render!"
echo "📋 Следуйте инструкциям в README.md"

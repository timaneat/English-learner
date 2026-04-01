#!/bin/bash

echo "🚀 Развертывание English Learner App"
echo "===================================="

# Проверка наличия git
if ! command -v git &> /dev/null; then
    echo "❌ Git не установлен. Установите Git и попробуйте снова."
    exit 1
fi

# Проверка статуса git
if [ -d ".git" ]; then
    echo "✅ Репозиторий Git найден"
else
    echo "❌ Это не Git репозиторий. Инициализируйте git:"
    echo "git init"
    echo "git add ."
    echo "git commit -m 'Initial commit'"
    exit 1
fi

# Проверка наличия изменений
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  Есть несохраненные изменения. Сохраните их:"
    echo "git add ."
    echo "git commit -m 'Update for deployment'"
    read -p "Продолжить без сохранения? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo ""
echo "Выберите платформу для развертывания:"
echo "1) Streamlit Cloud (Рекомендую - самый простой)"
echo "2) Railway (Django - очень просто)"
echo "3) Render (Django - бесплатно)"
echo "4) Heroku (Django - требует CLI)"
echo ""

read -p "Ваш выбор (1-4): " choice

case $choice in
    1)
        echo ""
        echo "🌟 Streamlit Cloud Deployment"
        echo "============================"
        echo ""
        echo "1. Перейдите на: https://share.streamlit.io"
        echo "2. Авторизуйтесь через GitHub"
        echo "3. Выберите репозиторий: timaneat/English-learner"
        echo "4. Главный файл: streamlit_app.py"
        echo "5. Requirements: requirements_streamlit.txt"
        echo "6. Нажмите Deploy!"
        echo ""
        echo "✅ Готово! URL будет вида: https://english-learner.streamlit.app"
        ;;
    2)
        echo ""
        echo "🚂 Railway Deployment"
        echo "===================="
        echo ""
        echo "1. Перейдите на: https://railway.app"
        echo "2. Авторизуйтесь через GitHub"
        echo "3. Выберите репозиторий: timaneat/English-learner"
        echo "4. Railway автоматически настроит Django"
        echo "5. Нажмите Deploy"
        echo ""
        echo "✅ Готово! Railway предоставит URL автоматически"
        ;;
    3)
        echo ""
        echo "🎨 Render Deployment"
        echo "==================="
        echo ""
        echo "1. Перейдите на: https://render.com"
        echo "2. Авторизуйтесь через GitHub"
        echo "3. Создайте 'Web Service'"
        echo "4. Выберите репозиторий: timaneat/English-learner"
        echo "5. Настройки:"
        echo "   - Runtime: Python 3"
        echo "   - Build: pip install -r requirements.txt"
        echo "   - Start: gunicorn english_learner.wsgi:application --bind 0.0.0.0:\$PORT"
        echo ""
        echo "✅ Готово! Render предоставит URL"
        ;;
    4)
        echo ""
        echo "🟣 Heroku Deployment"
        echo "==================="
        echo ""

        # Проверка Heroku CLI
        if ! command -v heroku &> /dev/null; then
            echo "❌ Heroku CLI не установлен."
            echo "Установите: brew install heroku/brew/heroku"
            echo "Или скачайте: https://devcenter.heroku.com/articles/heroku-cli"
            exit 1
        fi

        echo "Создание Heroku приложения..."
        heroku create english-cards-$(date +%s) --region eu

        echo "Добавление PostgreSQL..."
        heroku addons:create heroku-postgresql:hobby-dev

        echo "Отправка кода на Heroku..."
        git push heroku main

        echo ""
        echo "✅ Готово! Проверьте URL в Heroku dashboard"
        ;;
    *)
        echo "❌ Неверный выбор. Запустите скрипт снова."
        exit 1
        ;;
esac

echo ""
echo "🎉 Удачного развертывания!"
echo "📚 Не забудьте поделиться ссылкой с друзьями!"

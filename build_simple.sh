#!/usr/bin/env bash
# Simplified build script for Render
set -o errexit

echo "🔧 Starting simplified build..."

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Verify installations
python -c "import django; print('Django OK')"
python -c "import gunicorn; print('Gunicorn OK')"
python -c "import whitenoise; print('WhiteNoise OK')"

# Collect static files
python manage.py collectstatic --no-input --clear

# Run migrations
python manage.py migrate

# Optional: load initial data
python manage.py loaddata cards/fixtures/initial_words.json 2>/dev/null || echo "No initial data"

echo "✅ Build completed!"
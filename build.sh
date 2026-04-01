#!/usr/bin/env bash
# exit on error
set -o errexit

echo "🚀 Starting build process..."

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Verify Django installation
echo "🔍 Verifying Django installation..."
python -c "import django; print(f'Django version: {django.VERSION}')"

# Collect static files
echo "🎨 Collecting static files..."
python manage.py collectstatic --no-input --clear

# Run migrations
echo "🗄️  Running migrations..."
python manage.py migrate --verbosity=1

# Load initial data (optional, won't fail if file doesn't exist)
echo "📚 Loading initial data..."
python manage.py loaddata cards/fixtures/initial_words.json || echo "⚠️  Initial data not loaded (this is OK)"

# Run system checks
echo "✅ Running system checks..."
python manage.py check --deploy

echo "🎉 Build completed successfully!"

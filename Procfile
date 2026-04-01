web: python manage.py runserver 0.0.0.0:$PORT --noreload
release: python manage.py migrate && python manage.py loaddata cards/fixtures/initial_words.json

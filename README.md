git clone https://github.com/Baskearavind/college-django.git

cd college-django

python -m venv venv

venv\Scripts\activate

pip install django

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

Starting development server at http://127.0.0.1:8000/

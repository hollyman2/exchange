короче штобы запустить это чудо надо в терминале 
pipenv shell
pipenv install django
pipenv install django-allauth==0.52.0
pipenv install django-taggit
cd exchange
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

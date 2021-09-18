# django-product-hunt

## Getting Started

1. Clone the repository
```bash
$ git clone https://github.com/vengadalagarsamy/django-product-hunt.git
```
2. Enter the project folder
```bash
$ cd django-product-hunt/
```
3. Install django onto your machine using ‘pip’ or ‘pip3’
```bash
$ pip3 install django
```
3. Make migrations and collect necessary static files for the site
```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py collect static
```
4. Create a superuser for admin control. Admin portal can be accessed via “localhost:8000/admin”
```bash
$ python3 manage.py createsuperuser
```
5. Run the server
```bash
$ python3 manage.py runserver
```

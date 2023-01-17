# ✈️ Digitravel

![python](https://img.shields.io/badge/Python-v3.9.6%20%2B-blue?logo=python)

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green) ![Tailwind](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
___
Django web application for city referencing built for an Openclassroom project using different API (Wikipedia, Mapbox, country-json).
## Requirements

Python 3.9.6 or higher, Django 4.1.4 or higher and pip3.  

### Tailwind CSS 

Install tailwind : https://tailwindcss.com/docs/installation?ref=material-tailwind  
Flowbite documentation : https://flowbite.com/docs/getting-started/django/

___

## Installation 

You need postgreSQL installed and create connection in ``settings.py``. Create ``.env``file to put your DB variables as it :  
```txt
DB_NAME=digitravel
DB_HOST=127.0.0.1
DB_PORT=5432
DB_USER=<user>
DB_PASSWORD=<password>
```
- Installation using Virtualenv :
```shell
python3 -m virutalenv env && source env/bin/activate
```
```shell
pip3 install -r requirements.txt
```

- Migrate and run server :
```shell
python3 manage.py migrate
```
```shell
python3 manage.py tailwind start
python3 manage.py runserver
```

## Generating data

To generate data use :  
```shell
python3 manage.py python3 post_inject
```
By default database id destroyed and it takes cities with minimum of 500'000 people.

Arguments :

```shell
optional arguments:
  -h, --help            show this help message and exit

  --min_population [MIN_POPULATION]
                        Select cities with X minimum of inhabitants | Default : 500000

  --max_population [MAX_POPULATION]
                        Select cities with X maximum of inhabitants
                        
  --keep_db             Add this if you don't want to delete() curent db before injection
```

## Mapbox API

If you want to use Mapbox map API, you need to generate API token and put it in ``.env``as : ``MAPBOX_API=<token>``  

___
## Run test

```shell
python3 manage.py test --pattern="test_*.py"
```
### Coverage :

```shell
python3 -m coverage run manage.py test --pattern="test_*.py" && python3 -m coverage report --rcfile=.coveragerc
```
Functional testing based on Chromedriver, download your version [here](https://chromedriver.chromium.org/downloads), drop file in ```/tests/test_functional/``` as ```chromedriver```.
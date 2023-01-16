# ✈️ Digitravel
![python](https://img.shields.io/badge/Python-v3.9.6%20%2B-blue?logo=python)

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green) ![Tailwind](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
___
## Requirements
Python 3.9.6 or higer, Django 4.1.4 or higher and pip3.
- Installation using Virtualenv :
```shell
python3 -m virutalenv env && source env/bin/activate
```
```shell
pip3 install -r requirements.txt
```
### Tailwind CSS 
Install tailwind : https://tailwindcss.com/docs/installation?ref=material-tailwind
Flowbite documentation : https://flowbite.com/docs/getting-started/django/

```shell
python3 manage.py tailwind start
```
## Run test 
```shell
python3 manage.py test --pattern="test_*.py"
```
### Coverage :
```shell
python3 -m coverage run manage.py test --pattern="test_*.py" && python3 -m coverage report --rcfile=.coveragerc
```

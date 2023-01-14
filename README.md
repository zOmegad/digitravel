# ✈️ Digitravel
![image](https://img.shields.io/badge/Python-v3.9.6%20%2B-blue?logo=python)

![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green) ![image](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)


# upvotes en back
p = Post.objects.get(id=2)
i = p.upvotes.filter(upvoted=True)
for t in i:
    print(t.user)

# tailwind
install tailwind : https://tailwindcss.com/docs/installation?ref=material-tailwind
Flowbite tailwind doc : https://flowbite.com/docs/getting-started/django/

```shell
python3 manage.py tailwind start
```
# Run test 
```shell
python3 manage.py test --pattern="test_*.py"
```
# Coverage :
```shell
python3 -m coverage run manage.py test --pattern="test_*.py" && python3 -m coverage report --rcfile=.coveragerc
```

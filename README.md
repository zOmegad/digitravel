# digitravel

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

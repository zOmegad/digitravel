# digitravel

# upvotes en back
p = Post.objects.get(id=2)
i = p.upvotes.filter(upvoted=True)
for t in i:
    print(t.user)

# tailwind
install tailwind : https://tailwindcss.com/docs/installation?ref=material-tailwind
Flowbite tailwind doc : https://flowbite.com/docs/getting-started/django/

```bash
python3 manage.py tailwind start
```
# Run test 
```python
python3 manage.py test --pattern="test_*.py"
```
# Coverage :
```python
python3 -m coverage run --rcfile=.coveragerc manage.py test
python3 -m coverage report --rcfile=.coveragerc
```

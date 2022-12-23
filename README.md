# digitravel

# upvotes en back
p = Post.objects.get(id=2)
i = p.upvotes.filter(upvoted=True)
for t in i:
    print(t.user)

# tailwind
install tailwind : https://tailwindcss.com/docs/installation?ref=material-tailwind
materiel tailwind doc : https://www.material-tailwind.com/docs/html/installation#installation

python3 manage.py tailwind start
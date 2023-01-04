from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from comment.models import Comment

@login_required
def create(request):
    new_comment = Comment()
    new_comment.body = request.POST.get("comment_body")
    new_comment.user_id = request.user.id
    new_comment.post_id = int(request.POST.get("post_id"))
    new_comment.save()
    return redirect('/post/{}'.format(int(request.POST.get("post_id"))))

@login_required
def destroy(request):
    cur_comment = Comment.objects.get(id=int(request.POST.get("comment_id")))
    post_id = int(request.POST.get("post_id"))
    if request.user == cur_comment.user:
        cur_comment.delete()
    return redirect('/post/{}'.format(post_id))

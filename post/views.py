from django.shortcuts import render
from post.models import Post
from comment.models import Comment
from review.models import Review
from django.core.exceptions import ObjectDoesNotExist
from watson import search as watson
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
import os
from dotenv import load_dotenv
import requests
import regex as re

def index(request):
    item = Post.objects.all()
    item_paginator = Paginator(item, 12)
    page_num = request.GET.get('page')
    #print(item.order_by().values_list('continent').distinct())
    try:
        page_obj = item_paginator.page(page_num)
    except (EmptyPage, PageNotAnInteger):
        page_obj = item_paginator.page(1)
    return render(request, 'post/index.html', {'post': page_obj})

def show(request, post_id):
    load_dotenv()
    item = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post_id=post_id)
    reviews = Review.objects.filter(post_id=post_id)
    wiki_text_link = requests.get("https://en.wikipedia.org/w/api.php?"
        "action=query&prop=extracts&titles="
        "{}&format=json".format(item.city))
    wiki_text_response = wiki_text_link.json()
    wiki_page_id = wiki_text_response["query"]["pages"]
    for i in wiki_page_id:
        page_id = i
        break
    wiki_result_brut = wiki_text_response["query"]["pages"][page_id]["extract"]
    regex = "(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"
    wiki_result = re.split(regex, wiki_result_brut)

    try:
        user_review = Review.objects.get(post_id=post_id, user_id=request.user.id)
    except ObjectDoesNotExist:
        user_review = None
    return render(request, 'post/show.html', 
            {'post': item, 
            'comments': comments,
            'user_review': user_review,
            'reviews': reviews,
            'post_score': item.post_score('score')["avg_rating"],
            'post_internet': item.post_score('internet')["avg_rating"],
            'post_fun': item.post_score('fun')["avg_rating"],
            'post_safety': item.post_score('safety')["avg_rating"],
            'post_cost': item.post_score('cost')["avg_rating"],
            'post_life_quality': item.post_score('life_quality')["avg_rating"],
            'post_hospitality': item.post_score('hospitality')["avg_rating"],
            'wiki_result': wiki_result[:3],
            'page_id': page_id,
            'map_api': os.getenv('MAPBOX_API')})

def search(request):
    query = request.GET.get('query')
    page_num = request.GET.get('page')
    item = watson.filter(Post, query)

    item_paginator = Paginator(item, 12)
    try:
        page_obj = item_paginator.page(page_num)
    except (EmptyPage, PageNotAnInteger):
        page_obj = item_paginator.page(1)

    return render(request, 'post/index.html', {'post': page_obj, 'query': query})
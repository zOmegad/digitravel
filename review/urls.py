from django.urls import path

from . import views


urlpatterns = [
    path('create/', views.create, name='create_review'),
    path('destroy/', views.destroy, name='destroy_review'),
]
from django.urls import path

from . import views


urlpatterns = [
    path("create/", views.create, name="create_comment"),
    path("destroy/", views.destroy, name="destroy_comment"),
]

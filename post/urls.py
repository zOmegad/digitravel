from django.urls import path


from . import views

from .views import page_not_found, server_error

handler404 = page_not_found
handler500 = server_error

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>/", views.show, name="show"),
    path("search/", views.search, name="search"),
]

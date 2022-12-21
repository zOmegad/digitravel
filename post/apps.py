from django.apps import AppConfig
from watson import search as watson

class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'
    def ready(self):
        Post = self.get_model("Post")
        watson.register(Post)

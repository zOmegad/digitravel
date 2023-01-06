from django.contrib import admin
from .models import Upvote

class UpvoteAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Upvote, UpvoteAdmin)
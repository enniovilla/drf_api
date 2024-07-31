from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'created_at', 'updated_at', 'image_filter')
    search_fields = ('title', 'content')
    list_filter = ('image_filter', 'created_at', 'owner')
    ordering = ('-created_at',)
    fields = ('title', 'content', 'image', 'image_filter', 'owner')

admin.site.register(Post, PostAdmin)

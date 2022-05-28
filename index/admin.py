from django.contrib import admin

# Register your models here.
from .models import Post, Category, Comment



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'meta_tags', 'meta_desc', 'image', 'tags', 'author', 'date','active',]
    prepopulated_fields = {'slug':('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'more', 'created_at', 'disc', 'hit',]
    prepopulated_fields = {'slug':('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'email', 'body', ]

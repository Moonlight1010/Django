from django.contrib import admin
from .models import Post, TwitterProfile

# Register your models here.

# first Method

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'date_posted', 'user')
#     list_display_links = ('title', 'date_posted')
#     search_fields = ('title', 'date_posted')
#     list_filter = ('title', 'date_posted')

# admin.site.register(Post, PostAdmin)

# Second Method
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_posted', 'user')
    list_display_links = ('title', 'date_posted')
    search_fields = ('title', 'date_posted')
    list_filter = ('title', 'date_posted')

@admin.register(TwitterProfile)
class TwitterProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_created')
    list_display_links = ('user',)
    list_filter = ('user',)
    search_fields = ('user', 'date_created')
    

from django.contrib import admin
from .models import *

# admin.site.register(Topic)
# admin.site.register(Content)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name","description","created_at") 
    search_fields = ("name",) 

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("title","topic","content","author") 
    list_filter = ("topic",)
    search_fields = ("title__startswith",)

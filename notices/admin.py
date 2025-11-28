from django.contrib import admin
from .models import Notice, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'expiry_date')
    list_filter = ('category',)
    search_fields = ('title', 'content')

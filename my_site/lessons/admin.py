from django.contrib import admin

from .models import Lessons, Category, Theme


class LessonsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'theme', 'is_published']
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_title']
    list_display_links = ('id', 'category_title')
    search_fields = ('title',)


class ThemeAdmin(admin.ModelAdmin):
    list_display = ['id', 'theme_title', 'category', 'slug']
    list_display_links = ('id', 'theme_title')


admin.site.register(Lessons, LessonsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Theme, ThemeAdmin)

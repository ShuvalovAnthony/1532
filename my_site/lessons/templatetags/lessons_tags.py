from django import template
from lessons.models import Category, Lessons, Theme
from django.db.models import Count
from django.db.models import Q

register = template.Library()


@register.simple_tag(name='course_list')
def get_course_list():
    return Category.objects.all()


@register.inclusion_tag('lessons/course_list.html')
def show_course_list(**kwargs):
    try:
        category_access = kwargs['category_access'] # получаем список категорий с course_list_main
    except:
        pass
    cats = ['python', 'unity3d', 'tech_svyazi'] # все существующие категории
    cats_nums = [1, 2, 3] # id категорий из бд для поиска, по порядку cats!
    for i in range(3):
        if category_access.count(cats[i]) == 0: # если в полученном списке нет категории - обнуляем поиск
            cats_nums[i] = 0
    f = (Q(pk=cats_nums[0]) | Q(pk=cats_nums[1]) | Q(pk=cats_nums[2])) # фильтр категорий (запрос)
    categories = Category.objects.annotate(cnt=Count('lessons')).filter(Q(cnt__gt=0) & f)

    return {"categories":categories, }


@register.inclusion_tag('lessons/themes_list.html')
def show_themes_list(**kwargs):
    theme_category = kwargs['theme_category']
    theme_id = {
        "Python": 1,
        "Unity 3D": 2,
        "Технологии связи": 3,
        "python": 1,
        "unity3d": 2,
        "tech_svyazi": 3
    }
    theme = Theme.objects.all().filter(category=theme_id[theme_category]).select_related('category')
    return {"theme": theme, }
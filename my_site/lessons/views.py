from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Lessons, Category
from user_lk.models import Profile

def main_page(request):
    return render(request, 'main_page.html', {'title': 'Главная страница'})


def completed_lessons(request):
    if request.POST:
        user_name = request.POST.get('user_name')
        user_id = request.POST.get('user_id')
        lesson_id = request.POST.get('lesson_id')
        user_profile = Profile.objects.get(pk=user_id)
        user_profile.completed_lessons += ',' + lesson_id
        user_profile.save()
        user_completed_lessons = list(user_profile.completed_lessons.split(','))
        if lesson_id in user_completed_lessons:
            return HttpResponse('complete', content_type='text/html')
        else:
            return HttpResponse('uncomplete', content_type='text/html')
    else:
        return HttpResponse('uncomplete', content_type='text/html')


def onload_completed_lessons(request): # гет запрос пример кнопки <a class="btn btn-primary"  id="ajax_test">GET</a>
                        # скрипт test.js
    if request.POST:
        print('onload post - ok')
        user_name = request.POST.get('user_name')
        user_id = request.POST.get('user_id')
        lesson_id = request.POST.get('lesson_id')
        user_completed_lessons = list(Profile.objects.get(pk=user_id).completed_lessons.split(','))
        if lesson_id in user_completed_lessons:
            return HttpResponse('complete', content_type='text/html')
        else:
            return HttpResponse('uncomplete', content_type='text/html')
    else:
        return HttpResponse('uncomplete', content_type='text/html')


class HomeLessons(ListView):
    '''Отображение списка всех уроков /courses'''
    model = Lessons  # модель
    template_name = 'course_list_main.html'  # имя шаблона
    context_object_name = 'lessons'  # имя для обращения
    paginate_by = 4  # кол-во уроков на странице

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        # вовзращает queryset с аргументами из фильтра
        return Lessons.objects.filter(is_published=True).select_related('category', 'theme')


class LessonsByCategory(ListView):
    '''Отображение списка уроков в категории /course/python/'''
    model = Lessons
    template_name = 'lessons_list.html'
    context_object_name = 'lessons'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(
            page_adress=self.kwargs['course_slug'])
        context['theme'] = context['title'].category_title
        return context

    def get_queryset(self):
        return Lessons.objects.filter(
            course_slug=self.kwargs['course_slug'],
            is_published=True,
            ).select_related('category', 'theme')


class LessonsByTheme(ListView):
    '''Отображение списка уроков по теме /course/python/peremennie'''
    model = Lessons
    template_name = 'lessons_list.html'
    context_object_name = 'lessons'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(
            page_adress=self.kwargs['course_slug'])
        context['theme'] = context['title'].category_title
        return context

    def get_queryset(self):
        return Lessons.objects.filter(
            theme_slug=self.kwargs['theme_slug'],
            is_published=True,
            ).select_related('category', 'theme')


class LessonPage(DetailView):
    model = Lessons
    template_name = 'lesson_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'lesson'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_queryset()[0]
        context['theme'] = self.kwargs['course_slug'] # берет адрес страницы чтобы отфильтровать тему в lessons_tags
        return context

    def get_queryset(self):
        return Lessons.objects.filter(
            course_slug=self.kwargs['course_slug'],
            slug=self.kwargs['slug'],
            is_published=True
        )

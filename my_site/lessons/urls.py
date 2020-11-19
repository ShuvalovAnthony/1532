from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='home'),
    path('courses', HomeLessons.as_view(), name='courses'),
    path('course/<str:course_slug>/', LessonsByCategory.as_view(), name='category'),
    path('course/<str:course_slug>/<str:theme_slug>', LessonsByTheme.as_view(), name='theme'),
    path('<str:course_slug>/<str:slug>/', LessonPage.as_view(), name='lesson_page'),
    path('onload_post/', onload_completed_lessons, name='onload_completed_lessons'),
    path('post/', completed_lessons, name='completed_lessons'),
]
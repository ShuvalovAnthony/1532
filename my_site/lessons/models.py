from django.db import models
from django.urls import reverse, reverse_lazy


class Lessons(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.SlugField(max_length=50, verbose_name='Адрес страницы', blank=True)
    course_slug = models.CharField(max_length=50, verbose_name='Адрес курса', blank=True)
    content = models.TextField(blank=True, verbose_name='Контент')
    preview_content = models.TextField(blank=True, verbose_name='Текст превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    icon = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Иконка')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    theme = models.ForeignKey('Theme', on_delete=models.PROTECT, null=True, verbose_name='Тема')
    theme_slug = models.CharField(max_length=50, verbose_name='Адрес темы', blank=True)


    def get_absolute_url(self):
        return reverse('lesson_page', kwargs={"course_slug": self.course_slug, "slug": self.slug})

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['created_at']


class Category(models.Model):
    category_title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')
    category_icon = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Иконка')
    category_preview_content = models.TextField(blank=True, verbose_name='Текст превью')
    page_adress = models.SlugField(max_length=20, blank=True)
    category_age = models.CharField(max_length=150, blank=True, verbose_name='Возраст')

    def get_absolute_url(self):
        return reverse('category', kwargs={"course_slug": self.page_adress})

    def __str__(self):
        return self.category_title

    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category_title']


class Theme(models.Model):
    theme_title = models.CharField(max_length=150, db_index=True, verbose_name='Тема')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    slug = models.SlugField(max_length=50, verbose_name='Слаг темы', blank=True)
 
    def get_absolute_url(self):
        return reverse('theme', kwargs={"course_slug": self.category.page_adress,
         "theme_slug": self.slug,
         })

    def __str__(self):
        return self.theme_title

    class Meta():
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['theme_title']
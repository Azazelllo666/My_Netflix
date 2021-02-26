from django.contrib import admin
from django.utils.safestring import mark_safe

from movie.models import Category, Genre, Actor, Movie, MovieShots, RatingStar, Rating, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("name", "url", "id")


class ReviewInline(admin.TabularInline):
    """Класс для вывода отзывов на вкладке фильмы"""
    model = Reviews
    extra = 0
    readonly_fields = ("name", "email", "parent")


class MovieInline(admin.TabularInline):
    """Вывод фильмов во вкладках актеры и режиссеры"""
    model = Movie.actors.through
    extra = 0


class MovieShotsInline(admin.TabularInline):
    """Вывод фильмов во вкладках актеры и режиссеры"""
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="120"')

    get_image.short_description = "Изображение"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ("name", "category", "year", "url", "draft")  # Что отобразить в админке
    list_filter = ("category", "year")  # По какому столбцу создать фильтр
    search_fields = ("name", "category__name")  # По какому столбцу сделать поиск
    inlines = [MovieShotsInline, ReviewInline]  # Чтобы в фильмах выводили отзывы к ним
    save_on_top = True  # Чтобы меню "сохранить" было вверху, а не внизу
    save_as = True  # Добавить в меню "сохранить" новую кнопку "сохранить как новый объект"
    list_editable = ("draft",)  # Чтобы чек-бокс сделать активным на странице
    readonly_fields = ('get_image',)
    fieldsets = (
        (None, {
            'fields': (('name', 'tagline', 'category'),)
        }),
        (None, {
            'fields': ('description', ('poster', 'get_image'))
        }),
        (None, {
            'fields': (('year', 'world_premier', 'country'),)
        }),
        ('Актеры, режисеры и жанр', {
            'classes': ('collapse',),
            'fields': (('actors', 'producers', 'genres',),)
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
        ('Опции', {
            'fields': (('url', 'draft'),)
        }),
    )  # Настройка отображения

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="120"')

    get_image.short_description = ""


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("movie", "text", "name", "email", "parent")
    list_display_links = ("movie", "text")  # Какой столбец сделать ссылкой
    readonly_fields = ("name", "email", "parent")  # Какие столбцы сделать не изменяемыми


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ('name', 'url')
    search_fields = ("name", "movie__name")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Актёры"""
    list_display = ('name', 'age', 'calc_age', 'get_image')
    search_fields = ('name',)
    inlines = [MovieInline]
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ('movie', 'ip')


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ('title', 'movie', 'get_image')
    list_filter = ('movie',)
    search_fields = ('title', 'movie__name')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


admin.site.register(RatingStar)

admin.site.site_title = 'My_Netflix'
admin.site.site_header = 'My_Netflix Администрирование сайта'

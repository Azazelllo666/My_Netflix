from django.contrib import admin

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


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ("name", "category", "year", "url", "draft")  # Что отобразить в админке
    list_filter = ("category", "year")  # По какому столбцу создать фильтр
    search_fields = ("name", "category__name")  # По какому столбцу сделать поиск
    inlines = [ReviewInline]  # Чтобы в фильмах выводили отзывы к ним
    save_on_top = True  # Чтобы меню "сохранить" было вверху, а не внизу
    save_as = True  # Добавить в меню "сохранить" новую кнопку "сохранить как новый объект"
    list_editable = ("draft",)  # Чтобы чек-бокс сделать активным на странице
    fieldsets = (
        (None, {
            'fields': (('name', 'tagline', 'category'),)
        }),
        (None, {
            'fields': ('description', 'poster')
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
    list_display = ('name', 'age')
    search_fields = ('name', )
    inlines = [MovieInline]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ('movie', 'ip')


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ('title', 'movie')
    list_filter = ('movie',)
    search_fields = ('title', 'movie__name')


admin.site.register(RatingStar)

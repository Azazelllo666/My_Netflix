from django.db import models

from datetime import date


class Category(models.Model):
    """Категория"""
    name = models.CharField(name='Категория', max_length=150)
    description = models.TextField(name='Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Actor(models.Model):
    """Актёры и режиссеры"""
    name = models.CharField(name='Имя', max_length=100)
    age = models.DateField(name='Дата рождения', default=date.today)
    description = models.TextField(name='Описание')
    image = models.ImageField(name='Изображение', upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актёры и режиссеры'
        verbose_name_plural = 'Актёры и режиссеры'


class Genre(models.Model):
    """Жанры"""
    name = models.CharField(name='Имя', max_length=100)
    description = models.TextField(name='Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    """Фильмы"""
    name = models.CharField(name='Фильм', max_length=100)
    tagline = models.CharField(name='Слоган', max_length=100, default='')
    description = models.TextField(name='Описание')
    poster = models.ImageField(name='Постер', upload_to='movies/')
    year = models.PositiveSmallIntegerField(name='Дата выхода', default=2021)
    country = models.CharField(name='Страна', max_length=40)
    producers = models.ManyToManyField(Actor, verbose_name='режиссер', related_name='film_producer')
    actors = models.ManyToManyField(Actor, verbose_name='актеры', related_name='film_actors')
    genres = models.ManyToManyField(Genre, verbose_name='жанры')
    world_premier = models.DateField(name='Премьера в мире', default=date.today)
    budget = models.PositiveIntegerField(name='Бюджет', default=0, help_text='Указывать сумму в доллорах')
    fees_in_usa = models.PositiveIntegerField(name='Сборы в США', default=0, help_text='Указывать сумму в доллорах')
    fees_in_world = models.PositiveIntegerField(name='Сборы в Мире', default=0, help_text='Указывать сумму в доллорах')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField(name='Черновик', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MovieShots(models.Model):
    """Кадры из фильма"""
    title = models.CharField(name='Заголовок', max_length=100)
    description = models.TextField(name='Описание')
    image = models.ImageField(name='Изображение', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField(name='Значение', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField(name='IP адресс', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CharField, verbose_name='фильм')

    def __str__(self):
        return f'{self.star} | {self.movie}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField(name='Имя', max_length=100)
    text = models.TextField(name='Сообщение', max_length=100)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

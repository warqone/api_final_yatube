from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import LETTER_LIMIT, MAX_LENGTH

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Название группы', max_length=MAX_LENGTH)
    slug = models.SlugField('Слаг группы', unique=True)
    description = models.TextField('Описание группы')

    def __str__(self):
        return self.title[:LETTER_LIMIT]


class Post(models.Model):
    text = models.TextField('Текст поста')
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор поста',
    )
    image = models.ImageField(
        'Картинка для поста',
        upload_to='posts/',
        null=True,
        blank=True,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа поста',
    )

    class Meta:
        default_related_name = 'posts'

    def __str__(self):
        return f'Публикация от {self.author}: {self.text[:LETTER_LIMIT]}'


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор комментария',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Комментарий к посту',
    )
    text = models.TextField('Текст комментария')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        default_related_name = 'comments'

    def __str__(self):
        return f'Комментарий от {self.author}: {self.text}. Пост: {self.post}'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Подписка'
    )

    def __str__(self):
        return f'{self.user} подписан на: {self.following}.'

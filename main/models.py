from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.utils.text import slugify


def slugify_func(content):
    return slugify(content)


class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    file = models.FileField(upload_to='document/', verbose_name='Путь к файлу')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    slug = AutoSlugField(populate_from=slugify_func, unique=True, editable=False)
    
    def __str__(self):
        return f'{self.owner} {self.name}'
    
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
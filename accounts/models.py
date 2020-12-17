from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import AbstractTimeModel
from dictapp.models import WordTranslate
# Create your models here.

class MyUser(AbstractUser,AbstractTimeModel):
    unknown_words = models.ManyToManyField(WordTranslate,related_name='unknown_words',blank=True)
    known_words = models.ManyToManyField(WordTranslate,related_name='known_words',blank=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['created_at']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

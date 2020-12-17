from django.contrib import admin

# Register your models here.

from .models import WordTranslate,Word

admin.site.register(Word)
admin.site.register(WordTranslate)
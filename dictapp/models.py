from django.db import models
from base.models import AbstractTimeModel
# Create your models here.

LANG_CHOICES = (
    ("az", "Azerbaijan"),
    ("en", "English"),
)

class Word(AbstractTimeModel):
    word = models.CharField(max_length=120,unique=True)
    language = models.CharField(max_length=2,choices=LANG_CHOICES)

    def __str__(self):
        return "{} --- {}".format(self.word,self.language)

    class Meta:
        ordering = ['-created_at']


class WordTranslate(AbstractTimeModel):
    source = models.ForeignKey(Word,related_name='source_word',on_delete=models.CASCADE)
    target = models.ForeignKey(Word,related_name='target_word',on_delete=models.CASCADE)

    def  __str__(self):
        return "{} --- {}".format(self.source.word,self.target.word)

    class Meta:
        ordering = ['created_at']
        unique_together = ['source','target']

    def save(self,*args,**kwargs):
        if self.source != self.target:
            super(WordTranslate,self).save(*args, **kwargs)

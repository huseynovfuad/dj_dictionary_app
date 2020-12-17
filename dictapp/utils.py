import random
from .models import WordTranslate


def find_translate(request):
    w = WordTranslate.objects
    first_id = w.first().id
    last_id = w.last().id
    id_ = random.randint(first_id,last_id)
    translate = w.get(id=id_)
    if translate in request.user.known_words.all():
        return find_translate(request)
    else:
        return translate

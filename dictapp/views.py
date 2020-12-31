from django.shortcuts import render,redirect
from .models import WordTranslate
from .utils import find_translate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
from google_trans_new import google_translator
# Create your views here.

@login_required(login_url='/login/')
def home(request):
    context = {}
    if WordTranslate.objects.count() == request.user.known_words.count():
        context['completed_message'] = 'Bütün sözlər bilindi!'
    else:
        translate = find_translate(request)
        context['translate']=translate
    if request.method == 'POST':
        source = request.POST['hidden-source'].strip().lower()
        target = request.POST['target'].strip().lower()
        wordT = WordTranslate.objects.get(source__word=source)
        if target == wordT.target.word.strip().lower():
            request.user.known_words.add(wordT)
            messages.success(request, 'Correct Answer')
        else:
            request.user.unknown_words.add(wordT)
            messages.error(request, 'Wrong Answer')
        return redirect('home')
    context['word_count'] = WordTranslate.objects.count()
    context['known_count'] = request.user.known_words.count()
    return render(request,'home.html',context)

@login_required(login_url='/login/')
def reset(request):
    request.user.known_words.set([])
    return redirect('home')
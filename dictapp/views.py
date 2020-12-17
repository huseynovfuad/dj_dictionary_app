from django.shortcuts import render,redirect
from .models import Word,WordTranslate
from .utils import find_translate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
from google_trans_new import google_translator
# Create your views here.

@login_required(login_url='/login/')
def home(request):
    context = {}
    if list(WordTranslate.objects.all()) == list(request.user.known_words.all()):
        context['completed_message'] = 'All words completed!'
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
    return render(request,'home.html',context)



"""
    if request.method == 'POST':
        print(request.POST)
        source = request.POST['hidden-source'].strip().lower()
        target = request.POST['target']
        word_translate = WordTranslate.objects.filter(source__word = source).last()
        print(target)
        print(word_translate.target.word)
        if target == word_translate.target.word:
            #request.user.known_words.add(word_translate)
            messages.success(request, 'Correct Answer')
        else:
            #request.user.unknown_words.add(word_translate)
            messages.error(request, 'Wrong Answer')
        return redirect('home')
"""
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from read_text.models import Word,Input_text,Input_word,Count_word
import string
from collections import defaultdict
# Create your views here.

#def index(request):
#        return HttpResponse("Hello, world. You're at the read_text index.")

def display(request):
#    wrd_word = ['sein','Übertretung']
#    for wrd_word_i in range(len(wrd_word)):
#        if not Word.objects.filter(word=wrd_word[wrd_word_i]).exists():
#            wrd = Word(word=wrd_word[wrd_word_i])
#            wrd.save()
    return render(request,'template.tmpl',{'obj':Word.objects.all()})

def text_input(request):
    count_word()
    return render(request,'text_input.html',{'text':Input_text.objects.all(),\
            'word':Count_word.objects.exclude(count=0).order_by('-count')})

def count_word():
    Count_word.objects.all().delete()
    word_dict = defaultdict(int)
    for w in Input_word.objects.values():
       word_dict[w['text_word']] += 1
    for word in word_dict:
        if Word.objects.filter(word=word).exists():
            wrd = Count_word(word=word,count=word_dict[word])
            wrd.save()
    return

def submit_text(request):
    try:
        Input_text.objects.all().delete()
        Input_word.objects.all().delete()
        text = request.POST['input_text']
    except KeyError as ErrorDetail:
        text = "Try input text again. Error : ",ErrorDetail
        it = Input_text(text=text)
        it.save()
        return render(request,'text_input.html',{'text':Input_text.objects.all(),\
            'word':Input_word.objects.all()})
    else:
        it = Input_text(text=text)
        it.save()
        for wd in [word.strip(string.punctuation) for word in text.split()]:
            iw = Input_word(text_word=wd)
            iw.save()
        return HttpResponseRedirect('/read_text/text_input/')

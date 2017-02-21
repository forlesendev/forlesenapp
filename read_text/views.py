from django.shortcuts import render
from django.http import HttpResponse
from read_text.models import Word
# Create your views here.

#def index(request):
#        return HttpResponse("Hello, world. You're at the read_text index.")

def display(request):
    wrd_word = ['sein','haben','werden','koennen','muessen',\
    'sagen','machen','geben','kommen','sollen','wollen','gehen',\
    'wissen','sehen','lassen','stehen','finden','bleiben','liegen',\
    'heissen','denken','nehmen','tun','duerfen','glauben','halten',\
    'nennen','moegen','zeigen','fuehren','sprechen','sprechen',\
    'bringen','leben','fahren','meinen','fragen','kennen',\
    'gelten','stellen','spielen','arbeiten','brauchen','folgen',\
    'lernen','bestehen','verstehen','setzen','bekommen','beginnen']
    for wrd_word_i in range(len(wrd_word)):
        if not Word.objects.filter(word=wrd_word[wrd_word_i]).exists():
            wrd = Word(word=wrd_word[wrd_word_i])
            wrd.save()
    return render(request,'template.tmpl',{'obj':Word.objects.all()})

def text_input(request):
    return render(request,'text_input.html')

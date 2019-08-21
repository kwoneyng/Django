from django.shortcuts import render
from datetime import datetime
import random

# Create your views here.
def index(request):         # 첫번째 인자는 반드시 request가 온다. (사용자가 보내는 요청에 대한 정보)
    return render(request, 'index.html')    # render의 첫번째 인자도 반드시 request


def introduce(request):
    return render(request, 'introduce.html')


def dinner(request, name):
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'pick':pick,
        'name':name,
    }
    return render(request, 'dinner.html', context)


def image(request):
    image_url = 'https://picsum.photos/700'
    context = {
        'img_url':image_url,
    }
    return render(request, 'image.html', context)


def greeting(request, name):
    context = {
        'name':name,
    }
    return render(request, 'greeting.html', context)


def times(request, num1, num2):
    context = {
        'num1':num1,
        'num2':num2,
        'result':num1*num2,
    }
    return render(request, 'times.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Lift is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus':menus,
        'my_sentence':my_sentence,
        'messages': messages,
        'empty_list':empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)


def info(request):
    return render(request, 'info.html')


def student(request, name, age):
    context = {
        'name':name,
        'age':age,
    }
    return render(request, 'student.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)


def isitbirthday(request):
    datetimenow = datetime.now()
    context = {
        "datetimenow": datetimenow,
    }
    return render(request, 'isitbirthday.html', context)


def lotto(request):
    real_lotto = [21, 25, 30, 32, 40, 42]  # 870회차 로또 번호
    lottos = []
    lottos = random.sample(range(1,46),6)
    context = {
        'real_lotto':real_lotto,
        'lottos':lottos,
    }
    return render(request, 'lotto.html', context)


def search(request):
    return render(request, 'search.html')


def result(request):
    Category = request.GET.get('Category')
    query = request.GET.get('query')
    context = {
        'query':query,
        'Category':Category,
    }
    return render(request, 'result.html', context)


def lotto_pick(request):
    return render(request, 'lotto_pick.html')


def lotto_result(request):
    real_lotto = [21, 25, 30, 32, 40, 42]  # 870회차 로또 번호
    allotto = list(map(int, request.GET.get('lot').split()))
    context = {
        'allotto':allotto,
        'real_lotto':real_lotto,
    }
    return render(request, 'lotto_result.html', context)


def static_example(request):
    return render(request, 'static_example.html')


def static_example2(request):
    return render(request, 'static_example2.html')


def workshop(request):
    return render(request, 'workshop.html')


def workshop2(request):
    pull = request.GET.get('pull')
    context = {
        'pull':pull,
    }
    return render(request, 'workshop2.html', context)
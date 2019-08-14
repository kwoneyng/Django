from django.shortcuts import render
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
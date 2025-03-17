import random
from faker import Faker

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    my_name = 'seongjin'
    context = {
        'name': my_name,
    }
    return render(request, 'hello.html', context)

def lunch(request):
    menu = ['짜장면', '짬뽕', '탕수육']
    pick = random.choice(menu)
    context = {
        'pick': pick,
    }

    return render(request, 'lunch.html', context)

def lotto(request):
    pick = random.sample(range(1, 46), 6)
    pick.sort()
    join_pick = ' '.join(map(str, pick))
    context = {
        'pick': join_pick,
    }
    return render(request, 'lotto.html', context)

def profile(request, username):
    context = {
        'username': username,
    }
    return render(request, 'profile.html', context)

def cube(request, number):
    result = number ** 3
    context = {
        'number': number,
        'result': result,
    }
    return render(request, 'cube.html', context)

def articles(request):
    fake = Faker()
    fake_articles = []

    for _ in range(100):
        fake_articles.append(fake.text())

    context = {
        'fake_articles': fake_articles,
    }
    return render(request, 'articles.html', context)
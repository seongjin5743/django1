import random
from faker import Faker

from django.shortcuts import render

# index 페이지를 렌더링하는 뷰 함수
def index(request):
    return render(request, 'index.html')

# hello 페이지를 렌더링하는 뷰 함수
def hello(request):
    my_name = 'seongjin'
    context = {
        'name': my_name,
    }
    return render(request, 'hello.html', context)

# lunch 페이지를 렌더링하는 뷰 함수
def lunch(request):
    menu = ['짜장면', '짬뽕', '탕수육']
    pick = random.choice(menu)
    context = {
        'pick': pick,
    }
    return render(request, 'lunch.html', context)

# lotto 페이지를 렌더링하는 뷰 함수
def lotto(request):
    # 1부터 45까지의 숫자 중 6개를 랜덤으로 선택하여 정렬
    pick = random.sample(range(1, 46), 6)
    pick.sort()
    join_pick = ' '.join(map(str, pick))
    context = {
        'pick': join_pick,
    }
    return render(request, 'lotto.html', context)

# profile 페이지를 렌더링하는 뷰 함수
def profile(request, username):
    # 사용자 이름을 context에 추가
    context = {
        'username': username,
    }
    return render(request, 'profile.html', context)

# cube 페이지를 렌더링하는 뷰 함수
def cube(request, number):
    # 입력된 숫자의 세제곱을 계산
    result = number ** 3
    context = {
        'number': number,
        'result': result,
    }
    return render(request, 'cube.html', context)

# articles 페이지를 렌더링하는 뷰 함수
def articles(request):
    fake = Faker()
    fake_articles = []

    # 100개의 기사 생성
    for _ in range(100):
        fake_articles.append(fake.text())

    context = {
        'fake_articles': fake_articles,
    }
    return render(request, 'articles.html', context)
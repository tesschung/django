# pages/views.py
from django.shortcuts import render
from datetime import datetime
import random

# Create your views here.
def index(request):     #첫번째 인자는 반드시 request => 사용자가 보내는 요청에 대한 정보가 있다
    # 요청이 들어오면 'index.html'을 보여준다.
    return render(request, 'index.html')    # render의 첫번째 인자도 반드시 request

def introduce(request):
    return render(request, 'introduce.html')

# Template Variable Example
def dinner(request, name):
    menu = ['강남 더막창스', '역삼 노랑통닭', '양자강 차돌짬뽕']
    pick = random.choice(menu)
    context = {
        'pick': pick,
        'name': name,
    }
    # Django template로 context 전달
    return render(request, 'dinner.html', context)

def image(request):
    url = 'https://picsum.photos/200'
    context = {
        'url': url,
    }
    return render(request, 'image.html', context)

# greeting/IU/ => IU가 name에 값으로 들어간다.
def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'greeting.html', context)
    
def times(request, num1, num2):
    result = num1 * num2
    context = {
        'num1': num1,
        'num2' : num2,
        'result': result
    }
    return render(request, 'times.html', context)

def template_language(request):
    menu = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'life is short'
    messages = ['apple', 'banana', 'mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'menu': menu,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)

def isitbirthday(request, mybd):
    dt = datetime.now()
    dt_new = dt.strftime('%m-%d')
    todaymonth = dt.strftime('%m')
    todayday = dt.strftime('%d')

    res = 'True'
    if dt_new != mybd:
        res = 'False'
    
    context = {
        'mybd': mybd,
        'dt_new': dt_new,
        'res': res,
        'todaymonth': todaymonth,
        'todayday': todayday,
    }
    return render(request, 'isitbirthday.html', context)

def isitbirthday2(request, mybd):
    # today = datetime.now()

    context = {
        'mybd': mybd
    }
    return render(request, 'isitbirthday2.html', context)


def lotto(request):
    real_lotto = [21, 25, 30, 32, 40, 42] # 870회차로또 번호
    luckynumbers = random.sample(range(1,46), 6)

    context = {
        'real_lotto': real_lotto,
        'luckynumbers': luckynumbers,
    }
    return render(request, 'lotto.html', context)
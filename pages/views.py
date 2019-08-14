# pages/views.py
from django.shortcuts import render
import random

# Create your views here.
def index(request):     #첫번째 인자는 반드시 request => 사용자가 보내는 요청에 대한 정보가 있다
    # 요청이 들어오면 'index.html'을 보여준다.
    return render(request, 'index.html')    # render의 첫번째 인자도 반드시 request

def introduce(request):
    return render(request, 'introduce.html')

# Template Variable Example
def dinner(request):
    menu = ['강남 더막창스', '역삼 노랑통닭', '양자강 차돌짬뽕']
    pick = random.choice(menu)
    context = {
        'pick': pick,
    }
    # Django template로 context 전달
    return render(request, 'dinner.html', context)

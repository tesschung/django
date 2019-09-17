# pages/views.py
from django.shortcuts import render
from datetime import datetime
import random
import requests

# Create your views here.
def index(request):     #첫번째 인자는 반드시 request => 사용자가 보내는 요청에 대한 정보가 있다
    # 요청이 들어오면 'index.html'을 보여준다.
    return render(request, 'pages/index.html')    # render의 첫번째 인자도 반드시 request

def introduce(request):
    return render(request, 'pages/introduce.html')

# Template Variable Example
def dinner(request, name):
    menu = ['강남 더막창스', '역삼 노랑통닭', '양자강 차돌짬뽕']
    pick = random.choice(menu)
    context = {
        'pick': pick,
        'name': name,
    }
    # Django template로 context 전달
    return render(request, 'pages/dinner.html', context)

def image(request):
    url = 'https://picsum.photos/200'
    context = {
        'url': url,
    }
    return render(request, 'pages/image.html', context)

# greeting/IU/ => IU가 name에 값으로 들어간다.
def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'pages/greeting.html', context)
    
def times(request, num1, num2):
    result = num1 * num2
    context = {
        'num1': num1,
        'num2' : num2,
        'result': result
    }
    return render(request, 'pages/times.html', context)

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
    return render(request, 'pages/template_language.html', context)

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
    return render(request, 'pages/isitbirthday.html', context)

def isitbirthday2(request, mybd):
    # today = datetime.now()

    context = {
        'mybd': mybd
    }
    return render(request, 'pages/isitbirthday2.html', context)


def lotto(request):
    real_lotto = [21, 25, 30, 32, 40, 42] # 870회차로또 번호
    luckynumbers = random.sample(range(1,46), 6)
    luckynumbers = list(sorted(luckynumbers))
    context = {
        'real_lotto': real_lotto,
        'luckynumbers': luckynumbers,
    }
    return render(request, 'pages/lotto.html', context)

def search(request):
    return render(request, 'pages/search.html')

def result(request):
    query = request.GET.get('query')
    category = request.GET.get('category')
    context = {
        'query': query,
        'category': category,
    } 
    return render(request, 'pages/result.html', context)

def user_lotto_number(request):
    return render(request, 'pages/user_lotto_number.html')

def lotto_result(request):
    numbers = request.GET.get('numbers')
    numbers = list(sorted(list(map(str, numbers.split()))))

    lotto_round = request.GET.get('lotto_round')
    # real_lotto = [21, 25, 30, 32, 40, 42] # 870회차로또 번호
    # if numbers == real_lotto:
    #     res = '당첨'
    # else:
    #     res = '꽝'

    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    
    response = requests.get(url)
    #json 타입의 문서를 python dictionary로 parsing/ json()함수를 사용
    lotto_info = response.json()
    correct = 0
    winner = []
    #real_lotto_list = []
    for num in range(1,7):
        winner.append(str(lotto_info[f'drwtNo{num}']))
    
    ## 번호 교집합 개수 찾기
    if len(numbers) == 6:     # 사용자가 보낸 숫자가 6개가 맞는지 확인
        matched = 0                 # count용

        for number in numbers:# 사용자 숫자를 하나씩 확인하면서
            if number in winner:    # 당첨번호에 있는지 확인해서
                matched += 1        # 사용자의 번호가 있다면, 당첨시 matched를 1씩 증가시킨다 
        
        # print(matched)
        if matched == 6:
            result = '1등입니다.'
        elif matched == 5:
            if str(lotto_info['bnusNo']) in numbers:#bnusNo의 유무로 2등,3등 달라짐
                result = '2등입니다.'
            else:
                result = '3등입니다.'
        elif matched == 4:
            result = '4등입니다.'
        elif matched == 3:
            result = '5등입니다.'
        else:
            result = '맞추신 번호가 없습니다.'
    
    else:    
        result = '입력하신 숫자가 6개가 아닙니다.'

    
    context = {
        'numbers': numbers,
        'winner': winner,
        'lotto_round': lotto_round,
        # 'real_lotto': real_lotto,
        'result': result,
    }


    return render(request, 'pages/lotto_result.html', context)


def static_example(request):
    return render(request, 'pages/static_example.html')


def num(request):
    return render(request, 'pages/num.html')

def num_result(request):
    number = request.GET.get('number')
    context = {
        'number': number,
    }
    return render(request, 'pages/num_result.html', context)
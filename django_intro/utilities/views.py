# pages/views.py
from django.shortcuts import render

# Create your views here.
def index(request):     #첫번째 인자는 반드시 request => 사용자가 보내는 요청에 대한 정보가 있다
    # 요청이 들어오면 'index.html'을 보여준다.
    return render(request, 'utilities/index.html')    # render의 첫번째 인자도 반드시 request

from django.shortcuts import render, redirect
# 사용자가 입력하는 form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.http import require_GET, require_POST 
from django.contrib.auth import login as auth_login, logout as auth_logout 
# 이름이 함수와 동일해서 모듈이 실행되지 않는 것을 방지하기 위해서 as 로 모듈 이름을 지정해준다.
from IPython import embed

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        # 회원가입 로직
        # 사용자가 POST method로 보낸 요청을 아래와 같이 담는다
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            auth_login(request, user)
            # form을 저장한 후 articles의 index페이지로 넘어간다.
            return redirect('articles:index')
        
    else: # == GET
        # 회원가입하는 page
        form = UserCreationForm()

    context = {'form': form}
    # directory
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    # request.user.username == request
    if request.method == 'POST':
        # 위와 동일하게 작성한다.
        # 좀 특이함, 시험에 나옴
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 정보가 유효하다면 session을 만들어야한다.
            auth_login(request, form.get_user())
            # 로그인 하고나서는 다음 페이지를 들어가게 한다.
            # ?next=/articles/create/ 

            next_page = request.GET.get('next')
            # next값이 있다면 next_page로 가고, 그렇지 않으면 index로 간다.
            return redirect(next_page or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'accounts/login.html', context)

# login_required가 있으면 login 하자마자 logout이 되어버린다.
def logout(request):
    # request만 넣어주면 된다.
    auth_logout(request)
    return redirect('articles:index')

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')
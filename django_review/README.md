session

- **일정 시간동안** **같은 브라우저로 부터** 들어오는 일련의 요구를 하나의 상태로 보고 그 **상태를 유지하는 기술**

  즉, 웹 브라우저를 통해 웹 서버에 접속한 이후로 브라우저를 종료할 때 까지 유지되는 상태

  클라이언트가 Request를 보내면, 해당 서버의 엔진이 클라이언트에게 유일한 ID를 부여하는 데 이것이 세션ID다.

  **- 세션 프로세스**

  1. 클라이언트가 서버에 접속시 세션 ID를 발급

  2. 서버에서는 클라이언트로 발급해준 세션 ID를 쿠키를 사용해 저장 (JSESSIONID)

  3. 클라이언트는 다시 접속할 때, 이 쿠키(JSESSIONID)를 이용해서 세션ID값을 서버에 전달

  즉, 세션을 구별하기 위해 ID가 필요하고 그 ID만 쿠키를 이용해서 저장해놓는다. (쿠키사용) 쿠키는 자동으로 서버에 전송되니까 서버에서 세션아이디에 따른 처리를 할 수 있음

  예를들면 게시판에 글을 작성할 때 작성 버튼을 누르면 세션에 있는 아이디를 참조해서 작성자를 지정하게 한다.

  \- **세션 사용 사례**

  로그인 정보 유지

  

  https://jeong-pro.tistory.com/80

cookie

- 

cache

- 



elements

source



### 사용자 인증 기본구현

---



bash

```bash
$ python manage.py startapp accounts
(venv)
```


settings.py

```python
INSTALLED_APPS = [
    'articles',
    'accounts',

    'django_extensions',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

urls.py에 path를 include하고,

해당 앱에 urls.py를 만들어서 path를 추가한다.



```python
from django.shortcuts import render
# 사용자가 입력하는 form
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        # 회원가입 로직
        # 사용자가 POST method로 보낸 요청을 아래와 같이 담는다
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # form을 저장한 후 articles의 index페이지로 넘어간다.
            return redirect('articles:index')
        
    else: # == GET
        # 회원가입하는 page
        form = UserCreationForm()
        
    context = {'form': form}
    # directory
    return render(request, 'accounts/signup.html', context)
```



![캡처](../development/정승원_django_git/django/django_exam/images/캡처.JPG)





사용자 -> middle ware -> view

session아이디를 확인해서 request라는 객체를 통해서 로그인 되어있는지 안되어있는지 확인이 가능하다.



embed() 함수를 views.py에 작성하여 bash에서 다음과 같이 

들어오는 데이터에 대한 정보를 확인가능하다.

```bash
In [1]: request.user
Out[1]: <django.contrib.auth.models.AnonymousUser at 0x1b660174488>

In [2]: dir(request.user)
Out[2]:
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__int__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_groups',
 '_user_permissions',
 'check_password',
 'delete',
 'get_all_permissions',
 'get_group_permissions',
 'get_username',
 'groups',
 'has_module_perms',
 'has_perm',
 'has_perms',
 'id',
 'is_active',
 'is_anonymous',
 'is_authenticated',
 'is_staff',
 'is_superuser',
 'pk',
 'save',
 'set_password',
 'user_permissions',
 'username']

# 로그인 되어있는 상태인지 아닌지 아래와 같이 확인 가능하다.
In [3]: request.user.is_anonymous
Out[3]: True

In [4]: request.user.username
Out[4]: ''

In [5]: exit()
```












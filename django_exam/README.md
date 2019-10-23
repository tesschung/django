

장고

web framework

MTV - model - template - view





미완성된프로젝트,

장고를 runserver한 후

명세서에 나와있는 것처럼 에러들을 잡아내는 퀘스트형식

가상환경 설정

모듈 설치




# Django crud 구축하기

###  1. 가상 환경 생성 및 적용

---

### 1) 파이썬 버전 확인
##### 반드시 3.7.x 버전이 맞는지 확인 후 진행
```bash
$ python -V
Python 3.7.4
```

## 2) 가상환경 생성
```bash
##### python -m venv <가상환경 설치 경로>
$ python -m venv venv

kill terminal
ctr+shift+p -> python shift interpreter
python 3.7.4 64-bit('venv':venv)
```


## 3) 가상환경 적용
```bash
$ source venv/Scripts/activate
```

## 4) 버전 확인
```bash
(venv) # <- 가상환경 적용 시 git bash에서 해당 환경 이름이 표시된다.
$ python -V
Python 3.7.4
```

## 5) 설치된 모듈 확인
```bash
(venv)
$ pip list
Package    Version
---------- -------
pip        19.0.3
setuptools 40.8.0
```

### 6) pip upgrade
```bash
(venv)
$ python -m pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/8d/07/f7d7ced2f97ca3098c16565efbe6b15fafcba53e8d9bdb431e09140514b0/pip-19.2.2-py2.py3-none-any.whl (1.4MB)
    100% |████████████████████████████████| 1.4MB 7.3MB/s
Installing collected packages: pip
  Found existing installation: pip 19.0.3
    Uninstalling pip-19.0.3:
      Successfully uninstalled pip-19.0.3
Successfully installed pip-19.2.2
```

## 7) pip upgrade 확인
```bash
(venv)
$ pip list
Package    Version
---------- -------
pip        19.2.2
setuptools 40.8.0
```

### 7-1) django 설치
$ pip install django

### 7-2) 설치 목록 확인
$ pip freeze > requirements.txt


### 7-3) requirements 내의 module 설치
$ pip install -r requirements.txt

## 2. 환경 세팅

```python
# 1) 인터프리터 설정
Ctrl + Shift + P -> Python: Select Interpreter 선택
    
    
# 2) 환경 변수 세팅
.vscode의 settings.json을 바꾸어 준다.

{
    // 파이썬 환경 선택
    "python.pythonPath": "venv\\Scripts\\python.exe",
    // Django에서 사용되는 파일 타입에 대한 정의
    "files.associations": {
        "**/templates/*.html": "django-html",
        "**/templates/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },
    // Django-html에서도 html-emet을 적용
    "emmet.includeLanguages": {
        "django-html": "html"
    },
    // Django-html에서 tab size를 2칸으로 고정
    "[django-html]": {
        "editor.tabSize": 2
    },
}


# 3) gitignore 생성
- gitignore.io에 접속해서 python, windows, vscode 선택 후 생성 및 복사
- .gitignore 파일 생성 후 붙여넣기
```

## 3. django project 시작

```bash
# 1) django 모듈 설치
(venv)
$ pip install django
```

- Django를 설치한 순간부터 `django-admin`이라는 command를 사용할 수 있게 된다.
- 이 command를 통해 django project에 여러가지 명령을 할 수 있다.

```bash
# 2) start project

(venv)
$ django-admin startproject myproject .
```

- 현재 디렉토리에서 myproject라는 이름으로 프로젝트를 시작하겠다는 뜻.

- Django project naming

  - `-` 캐릭터는 사용할 수 없다.

  - python과 django에서 이미 사용되는 이름은 사용하지 않는다.

    (django라는 이름은 django 그 자체와 충돌이 발생하며, test라는 이름도 django 내부적으로 사용하는 모듈 이름)

- 프로젝트명 뒤에 .을 반드시 적어야 한다.



```bash
$ python manage.py runserver

# 3) make app

(venv)
$ python manage.py startapp articles
```

- manage.py를 통해 앱을 생성한다.



## 4. settings.py 설정

```python
# 1) app 등록
# app을 만든 후 INSTALLED_APPS에 항상 등록해 준다.

INSTALLED_APPS = [
    # Local apps
    'articles',

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

:star:

```python
# 2) 언어 및 시간대 설정

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

# 장고의 번역 시스템을 활성화 하는 여부를 확인한다
# False 라고 하는 경우, 한글로 나오지 않는다.
USE_I18N = True

USE_L10N = True

USE_TZ = True
```

```python
# 3) STATIC 파일과 MEDIA 파일의 경로를 지정한다.
# 최상단 위치(project 폴더와 동일한 위치)에 media, static 폴더를 생성해 놓아야 한다.

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```



## 5. app의 models.py 설정

```python
from django.db import models
from imagekit.processors import Thumbnail
from imagekit.models import ImageSpecField

			  #models.Model로 상속 
class Article(models.Model):
    # id(pk)는 기본적으로 처음 데이터 생성시 자동으로 만들어진다.
    # id = models.AutoField(primary_key=True)

    # 모든 필드는 기본적으로 NOT NULL => 비어있으면 안 된다.
    title = models.CharField(max_length=20)
    content = models.TextField()
    # black=True 아무런 값이 넘어오지 않아도 저장할 수 있다. 데이터 유효성과 관련되어 있음.
    # null: DB와 관련되어 있다.
    # '', Null
    # Textfield에는 Null을 넣지 말자는 게 content. 문자열 빈 값 저장은 null이 아니라 ''
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 90},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
```

:star: article에서의 참조키 중요

```python
class Comment(models.Model):
    # on_delete : 만약 1:n 관계에서 1이 삭제된다면 어떻게 처리할 것인지를 결정한다.
    # on_delete=models.CASCADE : 'Article이 삭제되면 Comment도 함께 삭제'
    # related_name == 'Article instance가 comment를 역참조 할 수 있는 이름을 정의. related_name이 없을 경우 comment_set이 참조 이름(default)'
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
	# 데이터를 위한 데이터
    class Meta:
        ordering = ['-pk']
```

- 1:N 관계에서 N에 해당하는 클래스는 외래키를 지정해주어야 한다.
- Meta class를 통해 가장 마지막에 만들어진 데이터가 처음에 위치하도록 설정할 수 있다.


```python
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField() # 내용이 길기때문에 textfield
    created_at = models.DateTimeField(auto_now_add=True)
    # datefield가 아니라 datetimefield 로 날짜와 시간을 같이 저장한다.
    # auto_now_add=True 처음 생성될때만

    updated_at = models.DateTimeField(auto_now=True)
    # auto_now=True 정보가 새로워질때마다
```

```bash
$ pip install django-extensions ipython
```

```python
INSTALLED_APPS = [
    'articles',
	
    # 등록
    'django_extensions',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



** 이미 데이터베이스에 데이터가 저장된 상태에서,

새로운 필드에 데이터를 추가해야하는 상황인 경우,

이전에 저장된 데이터들은 새로운 필드에 해당하는 정보가 없으므로 어떻게 이러한 문제를 해결할 수 있을까?

기존에 있는 데이터들의 새로운 필드 자리에는 아래와 같은 처리를 진행한다.

```bash
$ python manage.py shell_plus

In [1]: Article
Out[1]: articles.models.Article

In [2]: article = Article()

In [3]: article.title = '첫번째 타이틀'

In [4]: article.content = '첫번째 내용'

In [6]: article.save()
```

:star: 똑같이 models.py에서 필드를 추가하는데,

추가하고 **makemigrations**를 하면 **options**를 두개를 준다.

이전 데이터를 어떻게 할지 물어본다.

**1) 이전 데이터에 특정 데이터를 직접 정의**

**1 -> ' ' 하고 enter**

그 후 migrate 하면 실제 데이터베이스에 반영이 된다.

2) 나갔다가 필드에 default값을 추가



## 6. migrate

```bash
# 1) makemigrations를 통해 django에 model이 작성됐음을 알린다.
(venv)
$ python manage.py makemigrations
```



```bash
# 2) migrate로 django에게 model을 실제 DB에 작성하라고 명령한다.
(venv)
$ python manage.py migrate
```



## 7. admin 권한 설정

```python
from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at', )
```

```bash
(venv)

$ python manage.py createsuperuer
```


- createsuperuser 명령어를 통해 관리자 id를 만들 수 있다.



## 8. urls.py 

:star: 경로설정
```python
# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

# urls.py 끼리 맵핑
urlpatterns = [
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
]
```


- include를 추가해 각각의 app에 존재하는 urls.py로 접근할 수 있게 한다.



```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'
# www.domain.com/articles/___
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
]
```



## 9. 기본 html 템플릿(base.html) 만들기

```django
<!-- myproject 폴더 안에 templates 폴더를 생성하고, 거기에 base.html을 만든다.-->

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>{% block title %}{% endblock %}</title>
  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
  {% block body %}{% endblock %}
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```


- title과 body에 block을 만들어 놓는다.
- bootstarp과 javascript 코드를 추가해 활성화시킨다.

:star:

base.html을 작성후 반드시 settings.py에 등록해줘야 한다

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'review', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



## 10. forms.py

:star: 

```python
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=20,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter the titie...',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter the content...',
                'rows': 5,
                'cols': 30,
            }
        )
    )
```


- 데이터를 받게 될 form 양식을 articles/forms.py에 작성한다.

:star:

```python
# Meta class
```



## 11. index.html

```python
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

# 모든 article을 보여주는 페이지.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)
```


- model과 form을 import한다.



```django
<!-- index.html -->

{% extends 'base.html' %}


{% block title %}아티클::Articles{% endblock title %}

{% block body %}
<h1>Articles</h1>
<a href="{% url 'articles:create' %}">[New]</a>
<hr/>
{% for article in articles %}
<div>
  <h3>{{ article.pk }}. {{ article.title }}</h3>
  <p>{{ article.created_at }}</p>
  <a href="{% url 'articles:detail' article.pk %}">[Detail]</a>
</div>
{% endfor %}

{% endblock body %}
```



## 12. create.html

```python
# views.py

# GET으로 들어오면 생성하는 페이지 rendering
# POST로 들어오면 생성하는 로직 수행
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # is_vaild -> form이 유효할 때만 데이터를 받는다.
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article(title=title, content=content)
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    # GET 요청으로 들어왔다면 빈 폼을 보여준다.
    # POST 요청인데 사용자가 이상한 값을 입력했다면(.is_valid가 False) 그대로 담아서 다시 보낸다.
    context = {
        'form': form
        }
    return render(request, 'articles/create.html', context)
```

:star: method="POST", action ="{% url 'articles:create' %}" 

:star: action을 생략해도 된다. 자기자신을 보고, method가 있는 경우​  

```django
{% extends 'base.html' %}

{% block title %}Article::Create{% endblock title %}

{% block body %}
<form method="POST" action ="{% url 'articles:create' %}">
{{ form.as_p }}
{% comment %} <input type="text"><br>
<textarea cols="30" rows="10"></textarea><br> {% endcomment %}
<button type="submit">생성하기</button>
</form>
{% endblock body %}
```

- {{ form.as_p }}를 통해 form을 html 페이지에 삽입한다.

```python
from django.shortcuts import render
from .forms import ArticleForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        # Article을 생성해달라고 하는 요청
        form = ArticleForm(request.POST) # 사용자의 데이터를 가지고 오겠다는 뜻
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else: # GET
        # Article을 생성하기 위한 페이지를 달라고 하는 요청
        form = ArticleForm()
        context = {'form': form}
        return render(request, 'articles/create.html', context)
```



## 13. detail.html

```python
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```

- get_object_or_404로 데이터를 호출한다.



```django
{% extends 'base.html' %}

{% block title %}아티클 세부 정보::Article{% endblock title %}

{% block body %}
  <h1>{{ article.title }}</h1>
  <p>{{ article.created_at }}</p>
  <hr/>
  <p>{{ article.content }}</p>
  <hr/>
  <a href="{% url 'articles:index' %}">[뒤로 가기]</a>
  <a href="#">[수정하기]</a>
  <a href="#">[삭제하기]</a>
{% endblock body %}


```

```html
{% extends 'base.html' %}

{% block title %}Articles::Index{% endblock title %}

{% block body %} 
<a href="{% url 'articles:create' %}">[생성하기]</a>
{% for article in articles %}
<div>
<h3>{{ article.pk }}. {{ article.title }}</h3><br>
<a href="{% url 'articles:detail' article.pk %}">[상세보기]</a>
</div>
{% endfor %}

{% endblock body %}
```



특정 method만 허락할 수 있도록 

@require_GET

@require_POST



   ```bash
   python manage.py startapp accounts
   ```

2.  settings.py에 등록하기

   ```python
   INSTALLED_APPS = [
   
       # Local apps
       'articles',
       'accounts',
       # # Third party apps
       # 'django_extensions',
   
       # Django apps
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]
   ```

3.  review/urls.py에 accounts를 연결하는 작업

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('articles/', include('articles.urls')),
       path('accounts/', include('accounts.urls')),  # include의 의미가 accounts 앱에 있는 urls.py의 urlpatterns를 찾으라는 뜻이므로 accounts urls.py에 해당 변수가 있어야 한다.
       path('admin/', admin.site.urls),
   ]
   
   ```

4. accounts/urls.py 생성

# 2. 회원가입 구현

1. urls.py

   ```python
   from django.urls import path
   from . import views
   
   app_name = 'accounts'
   urlpatterns = [
       path('signup/', views.signup, name='signup' ),
   ]
   
   ```

2. views.py

   ```python
   from django.shortcuts import render, redirect
   from django.contrib.auth.forms import UserCreationForm  # django가 제공하는 로그인 관련 기능
   # Create your views here.
   
   
   
   def signup(request):
       if request.method == "POST":  # 포스트 요청을 받으면
           # 회원가입 해주세요
           form = UserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('articles:index')
           
       else: # get요청을 받으면 
           # 회원가입 가능한 창을 반환해 주세요
           form = UserCreationForm()
       context = {
           'form' : form,
       }
       return render(request, 'accounts/signup.html', context)
   ```

3. tempates/accounts 생성 후 signup.html 생성

   ```django
   {% extends 'base.html' %}
   
   {% block title %}Accounts::Signup
   {% endblock title %}
   
   {% block container %}
   <H2>회원가입</H2>
   {% comment %} view.signup에서  get 요청으로 이 페이지에 와있ㅎ기 때문에, 다시  form요청으로 보낼때는 action 이 필요없다.  {% endcomment %}
   <form  method="POST"> 
     {{ form.as_p }}
     {% csrf_token %}
     <input type="submit" value='회원가입'>
   </form>
   
   
   {% endblock container %}
   ```

4. 결과화면![1](C:\Users\student\Django\django_review2\images\1.JPG)

5. 잘 등록 되었는지 확인하기

   ```
   python manage.py createsuperuser
   ```

   ![캡처](C:\Users\student\Django\django_review2\images\캡처.JPG)

   - 파란색 동그라미가 새로 등록한 계정

# 3. 로그인 구현

1. urls.py

   ```python
   from django.urls import path
   from . import views
   
   app_name = 'accounts'
   urlpatterns = [
       path('signup/', views.signup, name='signup' ),
       path('login/', views.login, name='login'),
   ]
   ```

   

2. views.py 

   - 시나리오 : 로그인 창에서 로그인을 시도하는

   ```python
   def login(request):  # 로그인은 세션 데이터를 만드는 것
       if request.method == 'POST':
           form = AuthenticationForm(request, request.POST)
           if form.is_valid():
               auth_login(request, form.get_user())  # get_user(): 사용자의 정보를 주는 함수, AuthenticationForm메소드 안에만 있는 함수
               return redirect('articles:index')
       else:
           form = AuthenticationForm()
       context = {
           'form' : form
       }
       return render(request, 'accounts/login.html', context)
   ```

   - `AuthenticationForm` 만의 특이한 점 

   - `form = AuthenticationForm(request, request.POST)` 두개의 인자가 필요함.

   -         if form.is_valid():
                 auth_login(request, form.get_user())

   - `get_user()`: 사용자의 정보를 주는 함수, AuthenticationForm메소드 안에만 있는 함수

3. login.html

   ```django
   {% extends 'base.html' %}
   
   {% block title %}Accounts::Login
   {% endblock title %}
   
   {% block container %}
   <h2>로그인하기</h2>
   
     <form method="POST">
       {% csrf_token %}
       {{ form.as_p }}
       <button type="submit">로그인하기</button>
     </form>
     <form action=""></form>
   {% endblock container %}
   ```

4. 문제없이 로그인 했는지 확인하기![캡처2](C:\Users\student\Django\django_review2\images\캡처2.JPG)

- `sessionid`가 생성되어 있다면 정상적으로 로그인 성공했다는 뜻. `SQL EXPLORER` -> `django_seesion`을 확인해보면 다음과 같이 저장되어 있다.

5. 로그인 되어있는 상태를 사용자에게 확인해주기 위해 `base.html` 수정

   ```python
   <!DOCTYPE html>
   <html lang="ko">
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <meta http-equiv="X-UA-Compatible" content="ie=edge">
     <title>{% block title %}{% endblock title %}</title>
   </head>
   <body>
     <header>
       <h1>저희 페이지에 오신걸 환영합니다.</h1>
       <p>Hello, {{ user.username }}</p>
     </header>
     <a href="{% url 'articles:index' %}">[목록]</a>
   <hr>
   
     {% block container %}{% endblock container %}
   </body>
   </html>
   ```

   


## 4. 로그아웃

1. urls.py

   ```python
   path('logout/', views.logout, name='logout'),
   ```

   

1. views.py

   ```python
   from django.contrib.auth import logout as auth_logout # 로그아웃을 하기위한 로직을 임포트 한다.
   
   def logout(request):
       auth_logout(request)
       return redirect('articles:index')
   
   ```

   ## 5. middleware(개념 정리 다시하기)

   - ```python
     # request안에 저장되어 있는 정보 확인하기
     form Ipython import embed
     
     def index(request):
         embed()
         articles = Article.objects.all()
         
         return render(request, 'articles/index.html', {'articles': articles})
     
     ```
```
     
   - ```shell
     In [6]: dir(request.user)
     Out[6]:
     ['DoesNotExist',
      'EMAIL_FIELD',
      'Meta',
      'MultipleObjectsReturned',
      'REQUIRED_FIELDS',
      'USERNAME_FIELD',
     	......
      'is_active',
      'is_anonymous',
      'is_authenticated',
      
     In [8]: request.user.is_anonymous
     Out[8]: False
     
     In [9]: request.user.is_authenticated
     Out[9]: True
     
     In [10]: request.user.username
     Out[10]: 'dltlsgh5'
      
```

  - 위 정보를 이용해 각 views.py 에서 랜더하는 함수들에 각 각 조건을 부여하여 다른 화면을 보여주면 로그인 유뮤에 따라 기능이 다른 웹서비스를 제공할 수 있다.
   
- 즉, 로그인과 로그인 하기 전의 기능을 분리하기 위해 `base.html`과 `views.py`를 수정한다.
  
     ```django
     # base.html
         {% if  user.is_authenticated  %}
           <p>
             <span>Hello, {{ user.username }}</span>
             <a href="{% url 'accounts:logout' %}">[로그아웃]</a>
           </p>
         {% else %}
             <a href="{% url 'accounts:login' %}">[로그인]</a>
             <a href="{% url 'accounts:signup' %}">[회원가입]</a>
         
         {% endif %}
     
  ```
  
  - header 안에 다음과 같이 분리한다.
  
- `signup`, `login`  에  다음과 같이 분기를 만든다.
  
     ```python
     def signup(request):
         if request.user.is_authenticated:
             return redirect('articles:index')
     	......
         
     def login(request):  # 로그인은 세션 데이터를 만드는 것
         if request.user.is_authenticated:
             return redirect('articles:index')
     	......
  ```
  
     

## 6. Actions for authenticated user

- 로그인 상태인 유저만 게시글을 생성하고, 수정하고, 삭제할 수 있도록 관리한다.

1. articles/index.html -> if 문으로 로그인 확인 상태 or 비로그인 상태를 파악하여 관리한다.

   ```django
   {% extends 'base.html' %}
   
   {% block title %} Article::Index
   {% endblock title %}
   
   {% block container %}
   
     {% if user.is_authenticated %}
       <h2>Article List</h2>
       <a href="{% url 'articles:create' %}">[생성하기]</a>
       <hr>
     {% else %}
       <h4>로그인 해야 게시글을 만들 수 있습니다.</h4>
     {% endif %}
     {% for article in articles %}
       <div>
         <h3>{{ article.pk }}. {{ article.title }}</h3><a href="{% url 'articles:detail' article.pk%}">[자세히보기]</a>
       </div>
       <br>
     {% endfor %}
   
   {% endblock container %} 
   ```

2. articles/views.py

   ```python
   from django.contrib.auth.decorators import login_required
   
   @login_required  
   def create(request):
       
       if request.method == 'POST':
           # Article 생성 요청
           form = ArticleForm(request.POST)  #사용자의 데이터를 가져오겠다ㅓ.
   	......
   ```

   - `@login_required` : 로그인 상태에서만 다음의 함수를 실행할 수 있고, 로그인 상태가 아니라면 로그인 창을 불러와 로그인 하도록 유도하는 기능
   - 만약 계정관리 앱 이름이 `accounts`가 아니라면, `@login_required(<app이름>/<로그인url>)`로 설정해야지 로그인 페이지를 불러오게 된다.
   - 하지만 현재 로그인 view함수는 무조건 index페이지로 반환하는 로직이었다.

3. accounts/views.py

   ```python
   def login(request):  # 로그인은 세션 데이터를 만드는 것
       if request.user.is_authenticated:
           return redirect('articles:index')
   
       if request.method == 'POST':
           form = AuthenticationForm(request, request.POST)
           if form.is_valid():
               auth_login(request, form.get_user())  # get_user(): 사용자의 정보를 주는 함수, AuthenticationForm메소드 안에만 있는 함수
               
               next_page = request.GET.get('next') 
               return redirect(next_page or 'articles:index')  
       else:
           form = AuthenticationForm()
       context = {
           'form' : form
       }
       return render(request, 'accounts/login.html', context)
   
   
   ```

   - `next_page = request.GET.get('next')` : next라는 param를 달아 로그인 페이지로 보낸다. 

     ex) http://127.0.0.1:8000/accounts/login/?next=/articles/create/
   
   - ```python
     if next_page: 
     	return redirect(next_page)
     else:
   	 	return redirect('articles:index')
     ```

     -  url정보에 next페이지라는 애가 있으면! 넥스트페이지로 보내고, 아니면 인덱스로 보내달라는 로직
   -  next_page = 'articles/create/' 정보가 담겨있다.
   
- ```python
     return redirect(next_page or 'articles:index')
     ```
   
     - 위 로직과 동일한 코드

4. articles/templates/articles/detail.html

   ```django
   {% extends 'base.html' %}
   
   {% block title %}Article::Detail{% endblock title %}
   
   {% block container %}
   
   
   <h2>{{ article.title }}</h2>
   <p>{{ article.created_at }}</p>
   <p>{{ article.content }}</p>
   
   {% if user.is_authenticated %}
   
     <a href="{% url 'articles:update' article.pk %}">[수정하기]</a>
     <form action="{% url 'articles:delete' article.pk %}" method = 'POST'>
       {% csrf_token %}
       <button type="submit">삭제하기</button>  
     </form>
     <form action="{% url 'articles:comments_create' article.pk %}" method='POST'>
       {% csrf_token %}
       {{ form.as_table }}   <button type="submit">댓글작성</button>
     </form>
   
   {% endif %}
   <hr>
   {% for comment in comments %}
     <li> 
     {% if user.is_authenticated %}
       <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST"> 
         {% csrf_token %}
         <span>{{ comment.pk }}  {{ comment }} {{ comment.created_at }}</span>
         <button type="submit">댓글삭제</button>
       </form>
     {% else %}
       <span>{{ comment.pk }}  {{ comment }} {{ comment.created_at }}</span>
     {% endif %}
     </li>
   {% endfor %}
   {% endblock container %}
   ```

   - `{% if user.is_authenticated %}` : 사용자가 인증이 되어 있으면, `{% endif %}`까지 작성되어 있는 로직을 반환하라.
   - 로그인 하기 전 `detail`페이지 상태
   - 로그인 후 `detail`페이지 상태

## 7. 회원탈퇴

1. urls.py

   ```python
   path('delete/', views.delete, name='delete'),
   ```
   
2. views.py

   ```python
   from django.views.decorators.http import require_POST
   
   @require_POST
   def delete(request):
       if request.user.is_authenticated:
           request.user.delete()
       return redirect('articles:index')
   ```

   - `@require_POST` : 로그아웃을 하기  위한 로직을 임포트 한다.



## 8. 사용자 정보 변경

흐름

> UserChangeForm

유저 정보 수정 changeform

상속받은 changeform을 forms.py에서 커스터마이징

변경된 changeform으로 views.py에 import하여 코드 수정



> PasswordChangeForm

비밀번호 수정 changeform은 장고가 유저정보 수정과 별개를 두어서 

별개의 페이지를 제공하여

로직 작성하여 페이지 제공

추가로, 비밀번호 변경 이후에도 계속 로그인이 유지될 수 있도록 처리



> forms.html

template 통합하여 하나의 html으로 form을 전달 할 수 있도록 함



## 9. Article과 User간의 M:N 관계


#### Comment 와 User 간 1:N 관계 

```
# Comment 와 User 간 1:N 관계

- Comment 모델에 user 필드를 추가하여 1:N 관계를 형성한다.
  - 기존 생성되어있던 comment 가 있을 경우 임의의 사용자 정보로 채운다.
  
- View 함수에서 comment 생성 시 User 정보를 함께 저장한다.
- Article 상세보기 화면에서 Comment 정보 표현 시 작성자 이름도 함께 보여준다.
- Article 상세보기 화면에서 내가 작성한 Comment 라면 삭제하기 버튼을 보여준다.
- View 함수에서 comment 를 생성한 유저와 요청을 보낸 유저가 같을 경우에만 삭제하기 기능을 수행한다.
```

 한 유저가 작성한 댓글은 해당 유저에게만 속해있다.





#### User과 User간의 M:N 관계 

누가 누구랑 매칭이 되어있는지 또다른 테이블을 생성해서 만들어줘야 한다.

수강신청과 같다.

한 사람이 한 과목을 수강신청했다고 다른사람이 수강신청을 하지못하는 것은 아니다.

그래서 중개테이블을 이용하기로함



db / migrations를 모두 지운 상태에서 시작해야 한다.





#### AbstractBaseUser vs AbstractUser 비교

https://whatisthenext.tistory.com/128



django의 user model은 AbstractBaseUser와 AbstractUser를 상속받을 수 있다.

- 중계 모델은 doctor.reservation_set.all()과 같이 reservation이라는 중간 과정을 거쳐야 하는 점이 불편하다.
- ManyToMany는 doctor.patients.all()처럼 직접 접근할 수 있어서 편리



## 10. python manage.py shell_plus

```bash
$ python manage.py shell_plus

In [3]: doctor1 = Doctor.objects.create(name='scarlet')

In [4]: doctor2 = Doctor.objects.create(name='bae')

In [5]: patient2 = Patient.objects.create(name='jeong', doctor=doctor2)

In [6]: patient1 = Patient.objects.create(name='jason', doctor=doctor1)

In [7]: Reservation.objects.create(doctor=doctor1, patient=patient1)
Out[7]: <Reservation: jason번 환자 jason>

In [8]: doctor1.reservation_set.all()
Out[8]: <QuerySet [<Reservation: jason번 환자 jason>]>

# doctor1이 환자에 대한 정보를 가지고 오려면 어떻게 해야할까?
```



models.py의 Patient에 ManyToManyField를 작성한다.

```python
class Patient(models.Model):
    name = models.CharField(max_length=200)
    doctors = models.ManyToManyField(Doctor, related_name="patients") # patient.doctors.all()
    # Patient에서만 ManyToManyField가 가능하다

    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}번 환자 {self.name}'
```

```bash
In [1]: doctor1 = Doctor.objects.create(name='jason')

In [2]: patient1 = Patient.objects.create(name='john')

In [3]: doctor1
Out[3]: <Doctor: jason번 의사 jason>

# doctor1에 patients를 추가하는데, patient1이다.
In [4]: doctor1.patients.add(patient1)

In [5]: doctor1.patients.all()
Out[5]: <QuerySet [<Patient: john번 환자 john>]>

In [6]: patient1.doctors.all()
Out[6]: <QuerySet [<Doctor: jason번 의사 jason>]>

# 아래도 똑같이 동작
In [7]: patient1.doctors.add(doctor1)

# doctor1에 patient1을 제외
In [9]: patient1.doctors.remove(doctor1)

In [10]: patient1.doctors.all()
Out[10]: <QuerySet []>
```



### 프로젝트 지난주차 내일까지

### 월말평가 이번주 금(코드짜기)

- Django 게시글 + 댓글까지만 (미디어파일 사진파일 업로드는x)
- auth 관련 회원가입/로그인/로그아웃(회원삭제/수정/변경x)
  - 장고 프로젝트를 전달받고, 명세서에 맞게 작성
- Django 좋아요  M:N관계 기능
- 기능 구현해보면서 공부하는것이 중요
- follow 구현

### 과목평가 다음주 월(객관식)

- SQL + ORM
- SQL/쿼리 마크다운, 오늘 마크다운, SQL 슬라이드
- 디테일....



### Things to read

https://github.com/JaeYeopHan/Interview_Question_for_Beginner/tree/master/Python



https://github.com/JaeYeopHan/Interview_Question_for_Beginner/tree/master/DataStructure
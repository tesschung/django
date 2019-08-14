## Django

MDN web docs

https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Introduction

특징

**OPINIONATED!** 독선적이다.



MVC pattern

m : model 

v : view

c : controller



MTV

m : model 데이터 관리

t : template 사용자가 보는 화면

v : view 중간 관리자



## Django Setting

### 가상환경

새로운 장고 생성

- 프로젝트의 호환성, 의존성 확립

```bash
# 파이썬 버전 확인
# 반드시 3.7.x 버전이 맞는지 확인 후 진행
student@M702 MINGW64 ~/development/django/django_intro (master)
$ python -V
Python 3.7.4
(3.7.4)

# 가상환경 생성
# python -m venv < 가상환경 설치 경로 >
student@M702 MINGW64 ~/development/django/django_intro (master)
$ python -m venv venv
(3.7.4)

# 가상환경 적용
student@M702 MINGW64 ~/development/django/django_intro (master)
$ source venv/Scripts/activate
(venv)

# 파이썬 버전 확인
student@M702 MINGW64 ~/development/django/django_intro (master)
$ source venv/Scripts/activate
(venv) # 가상환경 적용 시 git bash에서 해당 환경 이름이 표시된다.
student@M702 MINGW64 ~/development/django/django_intro (master)
$ python -V
Python 3.7.4
(venv)

# 설치된 모듈 확인
(venv) # 라는 가상환경에서,
student@M702 MINGW64 ~/development/django/django_intro (master)
$ pip list
Package    Version
---------- -------
pip        19.0.3
setuptools 40.8.0
You are using pip version 19.0.3, however version 19.2.2 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
(venv)

# pip upgrade
(venv) 
$ python -m pip install --upgrade pip 

# pip upgrade 확인
(venv) 
$ pip list
```



---

### VS Code 및 기타 세팅

#### VS Code 파이썬 환경 선택

- VS Code Extensions에서 `Python`과 `Django`설치

- `ctrl + shift + p => python: select interpreter => 방금  생성한 가상환경을 선택(.\venv\Scripts\python.exe)`
  - .vscode/settings.json 파일이 생성되며 터미넣에서 자동으로 가상환경 적용되는 것을 확인

```bash
student@M702 MINGW64 ~/development/django/django_intro (master)
$ source c:/Users/student/development/django/django_intro/venv/Scripts/activate
(venv)
```

#### Git ignore 세팅

http://gitignore.io/

- gitignore.io에 접속해서 `python`, `django`, `windows`, `vscode ` 선택 후 생성
- touch .gitignore 파일 생성 후 붙여넣기



#### VS Code Django 환경 세팅

```json
{   
    // 파이썬 환경 선택 => 자동으로 해줌
    "python.pythonPath": "venv\\Scripts\\python.exe",
    
    // Django에서 사용되는 파일 타입에 대한 정의
    "files.associations": {
        "**/templates/*.html": "django-html",
        "**/templates/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },

    // Django-html에서도  html-emmet을 적용
    "emmet.includeLanguages": {"django-html": "html"},

    // django-html에서 tab size를 2칸으로 고정
    "[django-html]": {
        "editor.tabSize": 2
    }
}
```



---

### Start Django project

#### Django 설치 

```bash
student@M702 MINGW64 ~/development/django/django_intro (master)
$ pip install django
```

- Django를 설치한 순간부터 `django-admin`이라는 command를 사용할 수 있게 된다.
- 이 command를 통해 django project에 여러가지 명령을 할 수 있다.


### Start project
```bash
student@M702 MINGW64 ~/development/django/django_intro (master)
$ django-admin startproject django_intro .
(venv)
student@M702 MINGW64 ~/development/django/django_intro (master)
$ python manage.py runserver
```

- 현재 디렉토리에서 django_intro 라는 이름으로 프로젝트를 시작하겠다.
- Django project name
  - `-` 캐릭터는 사용될 수 없다.
  - python과 django에서 이미 사용되는 이름은 사용하지 않는다.
    - django 라는 이름은 django 그 자체와 충동하며, test라는 이름은 django 내부, 자체적으로 사용하는 이름

#### Run server

```bash
$ python manage.py runserver
```

- ctrl + C 커맨드로 종료
- 기본적으로 `local host: 8000`에서 실행된다.



manage.py == root



settings.py ! Important 대소문자

```python
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```



---

#### APP 생성

APP이란? 

user이라는 application에는 user관련만 담당한다. 

furniture이라는 application에는 furniture 관련만 담당한다.



결국 각각의 project별로 기능들이 구현되어 있다.

application을 만들어서 특정 project가 일을 할 수 있도록 만드는 것이다.



프로젝트/앱

앱: 

특정한 기능(블로그나 공공 기록물을 위한 데이터베이스나, 간단한 설문조사 앱)을 수행하는 웹 어플리케이션

프로젝트: 

이런 특정 웹 사이트를 위한 앱들과 각 설정들을 한데 묶어놓은 것 

다수의 앱을 포함할 수 있고, 앱은 다수의 프로젝트에 포함 가능

```bash
# application 생성
# python manage.py startapp < 문서이름 >

(venv) # 해당 가상환경에서,
student@M702 MINGW64 ~/development/django/django_intro (master)
$ python manage.py startapp pages
(venv)
```



**admin.py** 관리자페이지 customizing

apps.py app에 대한 정보가 입력되는 곳

```python
from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'pages'
```

**models.py** 데이터 베이스 관리, 저장할 데이터를 정의

tests.py 테스트 코드 파일들 존재

**views.py** 사용자에게 보여질 페이지를 담당하는 함수 정의



settings.py

위에서 부터 인식을 한다.

```python
# Application definition

INSTALLED_APPS = [
    # Local apps
    'pages', # 꼭 추가!해야 인식한다.
    
    # Third party apps
    
    # Django apps 마지막에 오도록 setting
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



templates folder을 생성해서 앞으로 코드를 작성할 예정



**기본순서!**

1) urls.py에서 특정 탬플릿이 rendering 될 수 있도록 mapping하는 것 생성

2) view.py에서 만들고자 하는함수로 페이지 생성

3) templates를 만든다 -> 해당 폴더에서 html을 작성





#### 실습

url: image/

view:

```python
def image(request):
	# image url을 context에 담아서 image.html에 전달
```

template: image.html // 전달받은 image 을 img태그 src속성에 담아서 랜덤이미지를 보여준다.





url: times/

- variable routing으로 숫자 2개를 각각 int타입으로 num1, num2이름으로 받는다.

view:

```python
def times(request, num1, num2):
    # 두 숫자를 곱한 result 변수와 num1, num2를 context에 담아서 times.html에 전달
```

template: times.html // 전달받은 context의 값들을 알맞게 표시한다.





https://docs.djangoproject.com/ko/2.2/ref/templates/language/




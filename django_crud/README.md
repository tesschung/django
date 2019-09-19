
## Django

### 가상환경

- 어떠한 프로그램을 만들 때, 독자적으로 파이썬의 고유 library 만을 써서 만들기도 하지만, 3rd patry library 를 사용하기도 한다. 즉, 의존성이 발생한다.
- 파이썬 환경 및 버전 등의 문제로 본인의 컴퓨터에서 잘 작동하던 프로그램도, 다른 환경에 설치했을 때 잘 돌아가리라는 보장을 할 수 없다.
- 때문에 특정 프로그램만을 실행하기 위한 파이썬 가상환경을 따로 만들어서, 그 환경 속에서 모듈을 관리하는 방식을 선택한다.

**가상환경 세팅**

- Scripts

### VS Code 및 기타 세팅

**VS Code 파이썬 가상환경 선택**

- `Ctrl + Shift + P` → `Python: Select Interpreter` → 방금 생성한 가상환경을 선택
- `.vscode/settings.json` 파일이 생성되고 가상환경 경로가 설정되어 있는지 확인, 터미널에서 자동으로 해당 가상환경이 적용 되는지 확인

**gitignore 세팅**

- [gitignore.io](https://www.gitignore.io/) 에서 프로그래밍 언어, 기술스택, OS 등 선택하여 알맞은 `.gitignore` 파일을 생성
- 생성된 파일을 `.gitignore` 파일에 붙여넣기

**VS Code Django 환경 세팅**

- `.vscode/settings.json` 파일에 django 관련 세팅을 추가 해준다.

:star: setting.py

```json
{
    "python.pythonPath": "venv\\Scripts\\python.exe",
    "files.associations": {
        "**/templates/*.html": "django-html",
        "**/templates/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements",
    },
    "emmet.includeLanguages": {"django-html": "html"},
    "[django-html]": {
        "editor.tabSize": 2,
    },
}
```



:star: django-admin startproject crud .



:star: setting.py

```
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```



:star: python manage.py startapp articles



:star: setting.py

가서 installedapp에 startapp으로 생성한 app 이름 추가





:star:    Model.py 

created_at = models.DateTimeField(**auto_now_add**=True) # add는 새로운 정보 추가시 처음에만 
updated_at = models.DateTimeField(**auto_now**=True) # 아무거나 정보 추가시 갱신

```python
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # add는 새로운 정보 추가시 처음에만 
    updated_at = models.DateTimeField(auto_now=True) # 아무거나 정보 추가시 갱신
```



:star: 모델을 변경후 장고에게 선언

$ python manage.py **makemigrations**

```bash
$ python manage.py makemigrations
Migrations for 'articles':
  articles\migrations\0001_initial.py
    - Create model Article
(3.7.4)
```



:star: 알린후 반영 (schema  생성)

$ python manage.py **migrate**

```bash
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, articles, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
```





:star: Page 생성

3가지 스탭

- urls.py 정의
- app내에 urls.py 생성후, 앱 내에서 path 생성 
- path 생성 후 views.py에서 해당 함수를 생성하여 mapping 해준다.
- mapping 후 해당하는 html을 만드는 templates 폴더를 생성하고, 그 안에 해당 app이름으로 폴더를 하나 더 만든다.
![templates](\images\templates.JPG)
- 그안에 html을 만든다.



:one:urls.py

from django.contrib import admin
from django.urls import path, **include**

urlpatterns = [
    :star:articles 로 들어왔다면 articles/urls.py로 이동
​    **path('articles/', include('articles.urls')),** 
​    path('admin/', admin.site.urls),
]

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # articles 로 들어왔다면 articles/urls.py로 이동
    path('articles/', include('articles.urls')), 
    path('admin/', admin.site.urls),
]
```



:two: html

앞에 꼭 /를 붙여야 동일한 application 내에서 이동한다.

new.html

```html
<form action="/articles/create/">
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>NEW ARTICLE</title>
</head>
<body>
  <h1>NEW ARTICLE</h1>
  <form action="/articles/create/">
  <input type="text" name="title"><br>
  <textarea name="content" cols="30" rows="10"></textarea><br>
  <button type="submit">생성하기</button>
  </form>
</body>
</html>
```



:three: 

```

```



:star: 

```

```





:star: 

```

```





:star: 

```

```



:star: 

```

```


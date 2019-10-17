# Comment 기능 구현

- Comment 모델을 만들어야 합니다.
  - content : 문자열
  - created_at : 시간
  - article : 참조키
- Comment 의 Create, Read, Delete 가 가능해야 합니다.
  - Comment 생성/삭제 동작의 경우 모두 POST 요청으로 동작합니다.
  - Comment 읽기(목록)는및 생성/삭제 동작은 Article 의 읽기(상세보기)에 있습니다.
  - Comment 생성 동작은 모두(View, Template 에서) ModelForm 으로 구현해야 합니다.

주어진 장고페이지를 보고,

오류를 보고 고쳐나가는 연습

에러가 발생하는 상황을 파악할 것

1. not defined

   특정 변수, import 모듈

2. NoReverseMatch

   url 태그를 사용해서 경로 이름으로 특정 경로로 갈 수 있도록 할때, 발생하는 문제

   경로는 알겠는데, argument가 찾아지지 않는 경우 발생한다.

https://docs.djangoproject.com/en/2.2/ref/exceptions/#transactionmanagementerror

3. auto_now_add=True
4. auto_now=True
5. NOT Null contraint   article id를 안넣음
6. URL 작성시 / 필요

* 스태틱파일 잘 불러올 수 있을까?
* base.html 경로 세팅 가능?
* DB 모델링 안보고 할 수 있나?
* form사용 방법
django공부

- test 시험 연습

1. 주어진 장고플젝을 가지고 오류 고쳐나가기! -> 디버깅 능력 필요 -> error message 읽을 수 있어야함. 상황파악해서 error들 고쳐나가야함.

2. ex. not defined: 특졍 변수가 선언되지 않았을 때, import되지 않았을 때

3. ex. NoReverseMatch: url테그를 이용해 특정 경로로 보낼 수 있도록할 때, 경로상 문제가 생겼을 때

4. static파일 경로는 나올 수 있음.  image는 없음. 범위: crud부터 comment까지

   

   

#### OperationalError 







### 1. about 팀 페이지

load static

```python
# 최상단에 static 폴더 생성 후,
# settings.py에서 최하단에
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# 이거를 base.html에 설정
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <tBLINEle>{% block title %}BLINE{% endblock title %}</title>
</head>
<body>
{% block body %} 

{% endblock body %} 
</body>
</html>
```



### 2. about 멤버 페이지

views에서 startings 대신 starting_members로 혹은 반대러

```python
# urls.py랑 views.py랑 함수 이름이 matching되는지 확인!
```

### 3. Admin 페이지

settings.py 에서 ko-kr 바꾸려고 했는데, 이미 바뀜

그래서 USE_I18N 을 True로 바꿈.

```python
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = True
```



### 4. Article List 페이지

목록 안 나옴.

block body 를 block container

```python
{% block container %}
<form method="POST" action="{% url 'articles:create' %}">
{% csrf_token %}
{{ form.as_p }}
<button type="submit">[Complete]</button>
</form>
{% endblock container %}
```



### 5. Article 수정

csrf_token

```python

```



### 6. Article 삭제

```python

```



### 7. Article 생성시 내용누락

내용누락

내용 모델 추가

마이그레이트

import도 고려

```python

```





### 8. Article 생성 및 수정 시간 출력

settings.py 에 TIME_ZONE = 'Asia/Seoul'



### 9. Comment 생성

```python
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        # 해당 article에 저장
        if form.is_valid():
            comment = Comment()
            content = form.cleaned_data.get('content')
            comment.content = content
            comment.article = article # 해당 article에 생성된 comment가 속하도록 저장
            comment.save()
            return redirect('articles:detail', article.pk)

    else:
        form = CommentForm()
    return render(request, 'articles:detail', {'form':form, 'article_pk': article_pk })
```



### 10. Comment 삭제

```python
def comment_delete(request, comment_pk, article_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```



### 11. 로그아웃

로그아웃이 import 안 되어있다.



### 12. base.html 경로설정

settings.py

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 이 부분
        'DIRS': [os.path.join(BASE_DIR, 'blind', 'templates')],
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


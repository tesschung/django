

# Django form

```python
form = Form(request.GET)
if form.is_valid():
    form.save()
```







---

```bash
student@M702 MINGW64 ~/development/정승원_django_git/django/django_form (master)
$ venv
(3.7.4)
student@M702 MINGW64 ~/development/정승원_django_git/django/django_form (master)
$ python -V
Python 3.7.4
(3.7.4)
student@M702 MINGW64 ~/development/정승원_django_git/django/django_form (master)
$ python -m venv venv
(3.7.4)

-> kill terminal,
-> ctrl + shift + p
	python interpreter 추가
	
student@M702 MINGW64 ~/development/정승원_django_git/django/django_form (master)
$ pip install django

student@M702 MINGW64 ~/development/정승원_django_git/django/django_form (master)
$ python -m pip install --upgrade pip
```

tess@naver.com

1234





projects 안의 templates는 장고가 인식하지 못하므로 settings.py에서 인식시켜준다.

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'myform', 'templates')],
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





form.py 생성

```python
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=20)
    content = forms.CharField()
```



view.py

들어오는 데이터에 대한 유효성검사로직 구현


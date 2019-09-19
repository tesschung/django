from django.shortcuts import render, redirect
from .models import Article

# articles의 메인페이지고, article list를 보여준다.
def index(request):
    articles = Article.objects.all() # 모든 정보를 가지고 와서 articles라는 변수에 담는다.
    # html로 전달
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context) 
    # render 순서를 잘 지켜야 한다.

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article
        }    
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

# new.html에서 사용자가 입력한 정보가 여기로 보내진다.
# /articles/new/의 new.html 의 form에서 전달받은 데이터들
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article() # 생성한 스키마의 새로운 인스턴스 생성
    article.title = title # 정보를 할당시켜준다.
    article.content = content
    article.save() # 저장
    # redirect를 사용해서 index로 이동
    return redirect(f'/articles/detail/{article.pk}/')

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect(f'/articles/')
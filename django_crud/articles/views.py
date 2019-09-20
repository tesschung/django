from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment

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
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comments': comments,
        }    
    return render(request, 'articles/detail.html', context)

# 입력페이지 제공
# GET /articles/create/
# def new(request):
        # return render(request, 'articles/new.html')
    
# new.html에서 사용자가 입력한 정보가 여기로 보내진다.
# /articles/new/의 new.html 의 form에서 전달받은 데이터들
# POST /articles/create/
def create(request):
    # 만약 GET 요청으로 들어오면 html 페이지 rendering
    # 아니라면 (POST일 경우) 사용자 데이터 받아서 article 생성
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article() # 생성한 스키마의 새로운 인스턴스 생성
        article.title = title # 정보를 할당시켜준다.
        article.content = content
        article.save() # 저장
        # redirect를 사용해서 index로 이동
        return redirect('articles:detail', article.pk)
    else:
        return render(request, 'articles/create.html')
# redirect(f'/articles/detail/{article.pk}/')

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # article = Article.objects.get(pk=article_pk)
    if request.method == 'POST': 
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)
# redirect(f'/articles/')

# /articles/5/update/
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # POST : 실제 Update 로직 수행
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        article.title = title # 정보를 할당시켜준다.
        article.content = content
        article.save() # 저장
        return redirect('articles:detail', article.pk)

    # GET : Update 를 하기위한 Form을 제공하는 페이지
    else: # POST가 아니라 GET이라면,
        context = {
            'article' : article
        }
        return render(request, 'articles/update.html', context)


def comments_create(request, article_pk):
    # article_pk에 해당하는 article에 새로운 comment 생성
    # 생성한 다음 article detail page로 redirect
    article = Article.objects.get(pk=article_pk)

    if request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment()
        comment.content = content
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.pk)
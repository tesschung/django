from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article
from django.views.decorators.http import require_GET, require_POST # 새로운 애들
from IPython import embed
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@require_GET
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

# login 했을때 create로 보내지도록
@login_required
def create(request): 
    if request.method == 'POST':
        # Article을 생성해달라고 하는 요청
        form = ArticleForm(request.POST) # 사용자의 데이터를 가지고 오겠다는 뜻
        # embed() # python shell 을나가면 다시 코드 진행
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        # else:
        #     context = {'form': form}
        #     return render(request, 'articles/create.html', context)

    else: # GET
        # Article을 생성하기 위한 페이지를 달라고 하는 요청
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/create.html', context)

@require_GET
def detail(request, articles_pk):
    # 사용자가 url에 적어보낸 article_pk를 통해 디테일 페이지를 보여준다.
    # Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=articles_pk) # 해당 article_pk를 찾는데 없으면, 사용자에게 해당 데이터가 없다고 404 status code를 제공
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

# login_required는 get요청으로 이루어지는 곳에서만 사용하면 된다.
@login_required
def update(request, articles_pk):
    article = get_object_or_404(Article, pk=articles_pk)
    # context = {'article': article}
    if request.method == 'POST':
        # Article을 생성해달라고 하는 요청
        form = ArticleForm(request.POST, instance=article) 
        # 사용자의 데이터를 가지고 오겠다는 뜻, + instance로 선언하면서 기존에 있는 article에 추가하겠다는 뜻
        # embed() # python shell 을나가면 다시 코드 진행
        if form.is_valid():
            form.save()
            return redirect('articles:detail', articles_pk)

    else: # GET
        # Article을 생성하기 위한 페이지를 달라고 하는 요청
        form = ArticleForm(instance=article) # form안에 특정 데이터를 넣은채로 form을 생성하겠다.
    context = {'form': form}
    return render(request, 'articles/update.html', context)

# 아래와 같이 @require_POST 처리를 해주어서 따로 if request.method == 'POST': 처리를 하지 않아도 된다.
@require_POST
# @login_required
# POST이므로 사용하지 않는다.
def delete(request, articles_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=articles_pk)
        article.delete()
        return redirect('articles:index')
    return HttpResponse('You are Unauthorized', status=401)
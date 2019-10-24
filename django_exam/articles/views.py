from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from django.views.decorators.http import require_GET, require_POST # 새로운 애들
from IPython import embed
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import get_user_model # 시험 외우기


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
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk) 
        # else:
        #     context = {'form': form}
        #     return render(request, 'articles/create.html', context)

    else: # GET
        # Article을 생성하기 위한 페이지를 달라고 하는 요청
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/create.html', context)

@require_GET
def detail(request, article_pk):
    # 사용자가 url에 적어보낸 article_pk를 통해 디테일 페이지를 보여준다.
    # Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk) # 해당 article_pk를 찾는데 없으면, 사용자에게 해당 데이터가 없다고 404 status code를 제공
    comments = article.comments.all()
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

# login_required는 get요청으로 이루어지는 곳에서만 사용하면 된다.
@login_required
def update(request, article_pk):

    article = get_object_or_404(Article, pk=article_pk)
    # context = {'article': article}

    # 동일한 사용자인 경우에만 다음을 진행
    if article.user == request.user:
        if request.method == 'POST':
            # Article을 생성해달라고 하는 요청
            form = ArticleForm(request.POST, instance=article) 
            # 사용자의 데이터를 가지고 오겠다는 뜻, + instance로 선언하면서 기존에 있는 article에 추가하겠다는 뜻
            # embed() # python shell 을나가면 다시 코드 진행
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article_pk)
        else:
            form = ArticleForm(instance=article)

    else: # GET
        # Article을 생성하기 위한 페이지를 달라고 하는 요청
        form = ArticleForm(instance=article) # form안에 특정 데이터를 넣은채로 form을 생성하겠다.
    context = {'form': form}
    return render(request, 'articles/update.html', context)

# 아래와 같이 @require_POST 처리를 해주어서 따로 if request.method == 'POST': 처리를 하지 않아도 된다.
@require_POST
# @login_required
# POST이므로 사용하지 않는다.
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if article.user == request.user:
            article.delete()
        else:
            return redirect('articles:index')
    return redirect('articles:index')


# 댓글을 생성하는 요청을 받는다.
@require_POST
def comments_create(request, article_pk):
    if request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article_id = article_pk
            # comment 생성시 user정보를 다음과 같이 저장한다.
            comment.user = request.user
            comment.save()
    return redirect('articles:detail', article_pk)

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.user == request.user: # 요청 받은 사용자인지 확인
            comment.delete()
        return redirect('articles:detail', article_pk)
    return HttpResponse('You are Unauthorized', status=401)



def like(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)

    # .exists()
    if article.liked_users.filter(pk=user.pk).exists(): # 0개가 아닌 1개라도 데이터가 존재한다면 True를 반환한다.
        user.liked_articles.remove(article)
    else:
        user.liked_articles.add(article)

    return redirect('articles:detail', article_pk)


def follow(request, article_pk, user_pk):
    # 로그인한 유저가 게시글 유저를 Follow or Unfollow 한다.
    user = request.user # 로그인 유저
    person = get_object_or_404() # 게시글 주인

    if user in person.followers.all():
        person.followers.remove(user)
    else:
        person.followers.add(user)
    return redirect('articles:detail', article_pk)



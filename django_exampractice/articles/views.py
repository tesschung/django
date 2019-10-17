from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# 생성 작업할 목록
'''
생성
html: index

'''

def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': articles})

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article(title=title, content=content)
            article.save()
            return redirect('articles:index')

    else:
        form = ArticleForm()
    return render(request, 'articles/create.html', { 'form':form })

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment.all()
    form = CommentForm()
    context = {'article': article, 'comments': comments, 'form': form, 'article_pk': article_pk }


    return render(request, 'articles/detail.html', context)

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

def comment_delete(request, comment_pk, article_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)


